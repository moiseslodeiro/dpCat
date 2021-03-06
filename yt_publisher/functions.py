# encoding: utf-8
import pickle
import base64
import httplib2
from urlparse import urljoin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from oauth2client.client import Storage as BaseStorage, OAuth2WebServerFlow, Error
from oauth2client import xsrfutil
from apiclient.discovery import build
from yt_publisher.models import Publicacion
from configuracion import config
from django.conf import settings

YOUTUBE_SCOPES = [ 'https://www.googleapis.com/auth/youtubepartner',
                   'https://www.googleapis.com/auth/youtube.upload' ]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

LICENSE_TEXTS = {
    'CR' : 'Todos los derechos reservados.',
    'MD' : 'Creative Commons: Reconocimiento - No Comercial (CC BY NC).\nhttp://creativecommons.org/licenses/by-nc/4.0/deed.es_ES',
    'SA' : 'Creative Commons: Reconocimiento - No Comercial - Compartir Igual (CC BY NC SA).\nhttp://creativecommons.org/licenses/by-nc-sa/4.0/deed.es_ES',
    'ND' : 'Creative Commons: Reconocimiento - No Comercial - Sin Obra Derivada (CC BY NC ND).\nhttp://creativecommons.org/licenses/by-nc-nd/4.0/deed.es_ES'
}

class Storage(BaseStorage):

    __STORAGE_OPTION_KEY__ = "YT_PUBLISHER_STORAGE"

    def locked_get(self):
        credentials = None

        raw = config.get_option(self.__STORAGE_OPTION_KEY__)
        if raw:
            credentials = pickle.loads(base64.b64decode(raw))
            credentials.set_store(self)

        return credentials


    def locked_put(self, credentials):
        config.set_option(self.__STORAGE_OPTION_KEY__, base64.b64encode(pickle.dumps(credentials)))

    def locked_delete(self):
        config.del_option(self.__STORAGE_OPTION_KEY__)

class UnauthorizedError(Error):
    pass

def get_flow():
    return OAuth2WebServerFlow(client_id = config.get_option('YT_PUBLISHER_CLIENT_ID'),
                               client_secret = config.get_option('YT_PUBLISHER_CLIENT_SECRET'),
                               scope = YOUTUBE_SCOPES,
                               redirect_uri = urljoin(config.get_option('SITE_URL'), reverse('oauth2callback')),
                               approval_prompt='force',
                               access_type = 'offline')


def get_authenticated_service():
    credential = Storage().get()
    if credential is None or credential.invalid == True:
        raise UnauthorizedError
    http = httplib2.Http()
    http = credential.authorize(http)
    return build("youtube", "v3", http=http)

def get_playlists():
    youtube = get_authenticated_service()

    data = list()

    next_page_token = ""
    while next_page_token is not None:
        playlists_response = youtube.playlists().list(
          mine=True,
          part="snippet",
          maxResults=50,
          fields="items(id,snippet(title)),nextPageToken",
          pageToken=next_page_token
        ).execute()

        for playlist in playlists_response["items"]:
            data.append((playlist['id'], playlist['snippet']['title']))

        next_page_token = playlists_response.get("nextPageToken")

    return data

def get_channel_data():
    youtube = get_authenticated_service()

    return youtube.channels().list(
        part="snippet",
        mine=True,
        fields="items(id,snippet(title,description,thumbnails(default)))"
    ).execute()['items'][0]

def get_all_uploads(channel_id):
    youtube = get_authenticated_service()

    # Obtiene la playlist de uploads
    playlist = youtube.channels().list(
        part = "contentDetails",
        id = channel_id,
        fields = "items(contentDetails(relatedPlaylists))"
    ).execute()['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Lista el contenido de la playlist
    data = list()

    next_page_token = ""
    while next_page_token is not None:
        list_response = youtube.playlistItems().list(
            part = "contentDetails",
            maxResults = 50,
            playlistId = playlist,
            fields = "nextPageToken,items(contentDetails)",
            pageToken=next_page_token
        ).execute()

        for video in list_response['items']:
            data.append(video['contentDetails']['videoId'])

        next_page_token = list_response.get("nextPageToken")

    return data

def get_video_data(videoid):
    youtube = get_authenticated_service()

    return youtube.videos().list(
        part = "snippet,status",
        id = videoid,
        fields = "items(id,snippet(title,description,thumbnails(high),tags,publishedAt),status(uploadStatus,privacyStatus))"
    ).execute()['items']

def get_all_video_data(channel_id):
    vid_list = get_all_uploads(channel_id)
    n = 0
    video_list = list()
    while(n < len(vid_list)):
        video_list += get_video_data(",".join(vid_list[n:n + 50]))
        n += 50

    return video_list

def get_all_public_video_data(channel_id):
    video_list = list()
    for i in get_all_video_data(channel_id):
        if i['status']['privacyStatus'] == 'public' and i['status']['uploadStatus'] == 'processed':
            video_list.append(i)
    return video_list

def create_playlist(title, description, privacy_status):
    youtube = get_authenticated_service()

    playlists_insert_response = youtube.playlists().insert(
        part = "snippet,status",
        body = dict(
            snippet = dict(
                title = title,
                description = description
            ),
            status = dict(
                privacyStatus = privacy_status
            )
        ),
        fields = "id"
    ).execute()

    return playlists_insert_response["id"]

def insert_video_in_playlist(videoid, playlistid):
    youtube = get_authenticated_service()

    youtube.playlistItems().insert(
        part = "snippet",
        body = dict(
            snippet = dict(
                playlistId = playlistid,
                resourceId = dict(
                    kind = 'youtube#video',
                    videoId = videoid
                )
            )
        ),
        fields = ""
    ).execute()

def error_handler(e, request):
    try:
        raise e
    except UnauthorizedError:
        messages.error(request, u'No existe una cuenta asociada para la publicación, debe configurar una para poder publicar')
        return HttpResponseRedirect(reverse("config_plugin"))
    except Error:
        credentials = Storage().get()
        try:
            credentials.revoke(httplib2.Http())
        except Error:
            Storage().delete()
        messages.error(request, u'Ha habido un error con cuenta de publicación, se debe volver a realizar la asociación')
        return HttpResponseRedirect(reverse("config_plugin"))

"""
Devuelve el número de puestos libres para iniciar el proceso de publicación.
"""
def available_slots():
    return int(config.get_option('YT_PUBLISHER_MAX_TASKS')) - Publicacion.objects.count_actives()

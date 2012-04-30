# encoding: utf-8
from django.shortcuts import render_to_response
from configuracion import config
from settings import MEDIA_ROOT
from cb_publisher.models import RegistroPublicacion

import urllib
import json
import os
import shutil
import hashlib
import tempfile
from datetime import datetime

def _remote_action(action, params = None):
    if params:
        params = urllib.urlencode(params)
    f = urllib.urlopen("%s/plugins/dpcat/%s.php" %  (config.get_option('CB_PUBLISHER_CLIPBUCKET_URL'), action), params)
    return f.read()

def publish(task):
    task.status = 'EXE' # esto se debería hacer desde fuera en caso de multithread.
    task.save()
    v = task.video
    d = json.loads(task.data)

    localfile = os.path.join(config.get_option('CB_PUBLISHER_LOCAL_DIR'), os.path.basename(v.fichero))
    remotefile = os.path.join(config.get_option('CB_PUBLISHER_REMOTE_DIR'), os.path.basename(v.fichero))
    data = {
        'user' : config.get_option('CB_PUBLISHER_USERNAME'),
        'pass' : config.get_option('CB_PUBLISHER_PASSWORD'),
        'file' : remotefile,
        'title' : d['title'],
        'description' : d['description'],
        'tags' : d['tags'],
        'category' : d['category'],
        'license' : d['license'],
    }

    shutil.copy(v.fichero, localfile)

    error_text = u"'%s' (%s)\n--\n\n" % (v, datetime.now())
    try:
        ret_data = json.loads(_remote_action('uploader', data))
    except ValueError:
        error_text += ret_data
        ret_data = None

    os.remove(localfile)

    if ret_data:
        if ret_data['cb_errors'] or ret_data['message']:
            if ret_data['cb_errors']:
                error_text += '--- Salida de error del clipbucket --\n'
                for line in ret_data['cb_errors']:
                    error_text += ' * ' + line + '\n'
            if ret_data['message']:
                error_text += '--- Salida de error del plugin --\n'
                error_text += ret_data['message'] + '\n'
        else:
            RegistroPublicacion(video = v, enlace = ret_data['vlink']).save()
            task.delete()
            return
        
    # Hubo algún error

    # Guarda el registro del error.
    (handle, path) = tempfile.mkstemp(suffix = '.pub.log', dir = MEDIA_ROOT + '/' + task.logfile.field.get_directory_name())
    task.logfile = task.logfile.field.get_directory_name() + '/' + os.path.basename(path)
    os.write(handle, error_text)
    os.close(handle)

    # Si se creó la publicación en el ClipBucket se borra.
    if ret_data['vid']:
        import time
        time.sleep(10)
        data = {
            'user' : config.get_option('CB_PUBLISHER_USERNAME'),
            'pass' : config.get_option('CB_PUBLISHER_PASSWORD'),
            'vid' : ret_data['vid']
        }
        _remote_action('delete_video', data)
    
    task.status = 'ERR'
    task.save()

def get_categories():
    categorias = json.loads(_remote_action('get_categories'))

    choices = list()
    def get_sub_categories(parent, level):
        for cat in categorias:
            if cat['parent_id'] == parent:
                choices.append((cat['category_id'], "- " * level  + cat['category_name']))
                get_sub_categories(cat['category_id'], level + 1)


    for cat in categorias:
        if int(cat['parent_id']) is 0:
            choices.append((cat['category_id'], cat['category_name']))
            get_sub_categories(cat['category_id'], 1)

    return choices

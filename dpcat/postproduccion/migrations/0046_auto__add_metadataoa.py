# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'MetadataOA'
        db.create_table('postproduccion_metadataoa', (
            ('creator', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('typical_age_range', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('video', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['postproduccion.Video'], unique=True)),
            ('contributor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('interactivity_level', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('learning_resource_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('educational_language', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('temporal', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('guideline', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('interactivity_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('valid', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ispartof', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('knowledge_areas', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.CharField')(default=u'Espa\xf1ol', max_length=255)),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('dificulty', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('unesco', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('typical_learning_time', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('semantic_density', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('rightsholder', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('venue', self.gf('django.db.models.fields.CharField')(default=u'San Crist\xf3bal de La Laguna, Tenerife (Espa\xf1a)', max_length=255)),
            ('audience', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('context', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('postproduccion', ['MetadataOA'])
    
        for i in orm.Metadata.objects.all():
            nm = orm.MetadataOA(
                creator = i.creator,
                typical_age_range = i.typical_age_range,
                video = i.video,
                contributor = i.contributor,
                interactivity_level = i.interactivity_level,
                learning_resource_type = i.learning_resource_type,
                educational_language = i.educational_language,
                title = i.title,
                temporal = i.temporal,
                guideline = i.guideline,
                source = i.source,
                interactivity_type = i.interactivity_type,
                valid = i.valid,
                location = i.location,
                ispartof = i.ispartof,
                type = i.type,
                knowledge_areas = i.knowledge_areas,
                description = i.description,
                language = i.language,
                purpose = i.purpose,
                dificulty = i.dificulty,
                date = i.date,
                unesco = i.unesco,
                typical_learning_time = i.typical_learning_time,
                semantic_density = i.semantic_density,
                keyword = i.keyword,
                license = i.license,
                created = i.created,
                rightsholder = i.rightsholder,
                venue = i.venue,
                audience = i.audience,
                context = i.context,
            )
            nm.save()
    
    def backwards(self, orm):
        
        # Deleting model 'MetadataOA'
        db.delete_table('postproduccion_metadataoa')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'postproduccion.cola': {
            'Meta': {'object_name': 'Cola'},
            'comienzo': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PEN'", 'max_length': '3'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postproduccion.Video']"})
        },
        'postproduccion.ficheroentrada': {
            'Meta': {'object_name': 'FicheroEntrada'},
            'fichero': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postproduccion.TipoVideo']", 'null': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postproduccion.Video']"})
        },
        'postproduccion.historicocodificacion': {
            'Meta': {'object_name': 'HistoricoCodificacion'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postproduccion.InformeProduccion']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'postproduccion.incidenciaproduccion': {
            'Meta': {'object_name': 'IncidenciaProduccion'},
            'aceptado': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'comentario': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'emisor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postproduccion.InformeProduccion']"})
        },
        'postproduccion.informeproduccion': {
            'Meta': {'object_name': 'InformeProduccion'},
            'aprobacion': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'fecha_grabacion': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha_produccion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_validacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'operador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'video': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['postproduccion.Video']", 'unique': 'True'})
        },
        'postproduccion.metadata': {
            'Meta': {'object_name': 'Metadata'},
            'audience': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'contributor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dificulty': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'educational_language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'guideline': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactivity_level': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'interactivity_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'ispartof': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'knowledge_areas': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "u'Espa\\xf1ol'", 'max_length': '255'}),
            'learning_resource_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'rightsholder': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'semantic_density': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'temporal': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'typical_age_range': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'typical_learning_time': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unesco': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'valid': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.CharField', [], {'default': "u'San Crist\\xf3bal de La Laguna, Tenerife (Espa\\xf1a)'", 'max_length': '255'}),
            'video': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['postproduccion.Video']", 'unique': 'True'})
        },
        'postproduccion.metadataoa': {
            'Meta': {'object_name': 'MetadataOA'},
            'audience': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'contributor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dificulty': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'educational_language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'guideline': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactivity_level': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'interactivity_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'ispartof': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'knowledge_areas': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "u'Espa\\xf1ol'", 'max_length': '255'}),
            'learning_resource_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'rightsholder': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'semantic_density': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'temporal': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'typical_age_range': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'typical_learning_time': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unesco': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'valid': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.CharField', [], {'default': "u'San Crist\\xf3bal de La Laguna, Tenerife (Espa\\xf1a)'", 'max_length': '255'}),
            'video': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['postproduccion.Video']", 'unique': 'True'})
        },
        'postproduccion.plantillafdv': {
            'Meta': {'object_name': 'PlantillaFDV'},
            'fondo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'postproduccion.previsualizacion': {
            'Meta': {'object_name': 'Previsualizacion'},
            'fichero': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['postproduccion.Video']", 'unique': 'True'})
        },
        'postproduccion.tecdata': {
            'Meta': {'object_name': 'TecData'},
            'duration': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'txt_data': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'video': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['postproduccion.Video']", 'unique': 'True'}),
            'xml_data': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'postproduccion.tipovideo': {
            'Meta': {'object_name': 'TipoVideo'},
            'alto': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'ancho': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mix': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'plantilla': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postproduccion.PlantillaFDV']"}),
            'x': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'y': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'postproduccion.token': {
            'Meta': {'object_name': 'Token'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instante': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'video': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['postproduccion.Video']", 'unique': 'True'})
        },
        'postproduccion.video': {
            'Meta': {'object_name': 'Video'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fichero': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plantilla': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postproduccion.PlantillaFDV']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'INC'", 'max_length': '3'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['postproduccion']

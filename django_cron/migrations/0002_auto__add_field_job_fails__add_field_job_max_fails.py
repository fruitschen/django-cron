# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Job.fails'
        db.add_column(u'django_cron_job', 'fails', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)

        # Adding field 'Job.max_fails'
        db.add_column(u'django_cron_job', 'max_fails', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Job.fails'
        db.delete_column(u'django_cron_job', 'fails')

        # Deleting field 'Job.max_fails'
        db.delete_column(u'django_cron_job', 'max_fails')


    models = {
        u'django_cron.cron': {
            'Meta': {'object_name': 'Cron'},
            'executing': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'django_cron.job': {
            'Meta': {'object_name': 'Job'},
            'args': ('django.db.models.fields.TextField', [], {}),
            'fails': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.TextField', [], {}),
            'kwargs': ('django.db.models.fields.TextField', [], {}),
            'last_run': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 12, 20, 31, 14, 737626)'}),
            'max_fails': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'queued': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'run_frequency': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1440'})
        }
    }

    complete_apps = ['django_cron']

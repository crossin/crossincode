# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sample'
        db.create_table(u'oj_sample', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3000)),
        ))
        db.send_create_signal(u'oj', ['Sample'])


    def backwards(self, orm):
        # Deleting model 'Sample'
        db.delete_table(u'oj_sample')


    models = {
        u'oj.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pre_code': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'test_code': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'oj.sample': {
            'Meta': {'object_name': 'Sample'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['oj']
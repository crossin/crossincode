# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quiz'
        db.create_table(u'oj_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=3000)),
            ('test_code', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'oj', ['Quiz'])


    def backwards(self, orm):
        # Deleting model 'Quiz'
        db.delete_table(u'oj_quiz')


    models = {
        u'oj.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_code': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['oj']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Quiz.pre_code'
        db.add_column(u'oj_quiz', 'pre_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=3000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Quiz.pre_code'
        db.delete_column(u'oj_quiz', 'pre_code')


    models = {
        u'oj.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pre_code': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'test_code': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['oj']
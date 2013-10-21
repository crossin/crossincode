# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'LearnedCourse'
        db.delete_table(u'school_learnedcourse')

        # Deleting model 'LearnedLesson'
        db.delete_table(u'school_learnedlesson')


    def backwards(self, orm):
        # Adding model 'LearnedCourse'
        db.create_table(u'school_learnedcourse', (
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Course'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Student'])),
            ('progress', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'school', ['LearnedCourse'])

        # Adding model 'LearnedLesson'
        db.create_table(u'school_learnedlesson', (
            ('status', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Lesson'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Student'])),
        ))
        db.send_create_signal(u'school', ['LearnedLesson'])


    models = {
        u'oj.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pre_code': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'test_code': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'school.course': {
            'Meta': {'object_name': 'Course'},
            'count_student': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'school.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'school.lesson': {
            'Meta': {'object_name': 'Lesson'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'count_answer': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'count_finished': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'count_question': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'count_student': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['oj.Quiz']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['school']
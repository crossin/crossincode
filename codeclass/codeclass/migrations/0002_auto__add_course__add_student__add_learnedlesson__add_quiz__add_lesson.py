# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'codeclass_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('count_student', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codeclass.Language'])),
        ))
        db.send_create_signal(u'codeclass', ['Course'])

        # Adding model 'Student'
        db.create_table(u'codeclass_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30, db_index=True)),
            ('exp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'codeclass', ['Student'])

        # Adding model 'LearnedLesson'
        db.create_table(u'codeclass_learnedlesson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codeclass.Student'])),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codeclass.Lesson'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
        ))
        db.send_create_signal(u'codeclass', ['LearnedLesson'])

        # Adding model 'Quiz'
        db.create_table(u'codeclass_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=3000)),
            ('test_code', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'codeclass', ['Quiz'])

        # Adding model 'Lesson'
        db.create_table(u'codeclass_lesson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=3000)),
            ('count_student', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('count_finished', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('count_question', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('count_answer', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codeclass.Course'])),
            ('quiz', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['codeclass.Quiz'], unique=True, null=True)),
        ))
        db.send_create_signal(u'codeclass', ['Lesson'])

        # Adding model 'LearnedCourse'
        db.create_table(u'codeclass_learnedcourse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codeclass.Student'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codeclass.Course'])),
            ('progress', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'codeclass', ['LearnedCourse'])

        # Adding model 'Answer'
        db.create_table(u'codeclass_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=3000)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codeclass.Student'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codeclass.Question'])),
        ))
        db.send_create_signal(u'codeclass', ['Answer'])

        # Adding model 'Question'
        db.create_table(u'codeclass_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=3000)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codeclass.Student'])),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codeclass.Lesson'], null=True)),
        ))
        db.send_create_signal(u'codeclass', ['Question'])

        # Adding model 'Language'
        db.create_table(u'codeclass_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'codeclass', ['Language'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table(u'codeclass_course')

        # Deleting model 'Student'
        db.delete_table(u'codeclass_student')

        # Deleting model 'LearnedLesson'
        db.delete_table(u'codeclass_learnedlesson')

        # Deleting model 'Quiz'
        db.delete_table(u'codeclass_quiz')

        # Deleting model 'Lesson'
        db.delete_table(u'codeclass_lesson')

        # Deleting model 'LearnedCourse'
        db.delete_table(u'codeclass_learnedcourse')

        # Deleting model 'Answer'
        db.delete_table(u'codeclass_answer')

        # Deleting model 'Question'
        db.delete_table(u'codeclass_question')

        # Deleting model 'Language'
        db.delete_table(u'codeclass_language')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'codeclass.answer': {
            'Meta': {'object_name': 'Answer'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codeclass.Student']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codeclass.Question']"})
        },
        u'codeclass.course': {
            'Meta': {'object_name': 'Course'},
            'count_student': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codeclass.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'codeclass.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'codeclass.learnedcourse': {
            'Meta': {'object_name': 'LearnedCourse'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codeclass.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'progress': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codeclass.Student']"})
        },
        u'codeclass.learnedlesson': {
            'Meta': {'object_name': 'LearnedLesson'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codeclass.Lesson']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codeclass.Student']"})
        },
        u'codeclass.lesson': {
            'Meta': {'object_name': 'Lesson'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'count_answer': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'count_finished': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'count_question': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'count_student': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codeclass.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['codeclass.Quiz']", 'unique': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'codeclass.question': {
            'Meta': {'object_name': 'Question'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codeclass.Student']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codeclass.Lesson']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'codeclass.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_code': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'codeclass.student': {
            'Meta': {'object_name': 'Student'},
            'exp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['codeclass']
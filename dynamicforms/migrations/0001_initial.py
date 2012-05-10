# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DynamicForm'
        db.create_table('dynamicforms_dynamicform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('dynamicforms', ['DynamicForm'])

        # Adding model 'DynamicField'
        db.create_table('dynamicforms_dynamicfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fields', to=orm['dynamicforms.DynamicForm'])),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('field_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('dynamicforms', ['DynamicField'])

    def backwards(self, orm):
        # Deleting model 'DynamicForm'
        db.delete_table('dynamicforms_dynamicform')

        # Deleting model 'DynamicField'
        db.delete_table('dynamicforms_dynamicfield')

    models = {
        'dynamicforms.dynamicfield': {
            'Meta': {'object_name': 'DynamicField'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['dynamicforms.DynamicForm']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'dynamicforms.dynamicform': {
            'Meta': {'object_name': 'DynamicForm'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['dynamicforms']
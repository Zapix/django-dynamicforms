# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DynamicField.help_text'
        db.add_column('dynamicforms_dynamicfield', 'help_text',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'DynamicField.help_text'
        db.delete_column('dynamicforms_dynamicfield', 'help_text')

    models = {
        'dynamicforms.dynamicfield': {
            'Meta': {'object_name': 'DynamicField'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['dynamicforms.DynamicForm']"}),
            'help_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
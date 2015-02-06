# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Gig.description'
        db.alter_column(u'quingenti_gig', 'description', self.gf('django.db.models.fields.CharField')(max_length=7000))

    def backwards(self, orm):

        # Changing field 'Gig.description'
        db.alter_column(u'quingenti_gig', 'description', self.gf('django.db.models.fields.CharField')(max_length=3000))

    models = {
        u'quingenti.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'quingenti.gig': {
            'Meta': {'object_name': 'Gig'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quingenti.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '7000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['quingenti']
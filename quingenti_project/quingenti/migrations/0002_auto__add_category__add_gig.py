# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'quingenti_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal(u'quingenti', ['Category'])

        # Adding model 'Gig'
        db.create_table(u'quingenti_gig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quingenti.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'quingenti', ['Gig'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'quingenti_category')

        # Deleting model 'Gig'
        db.delete_table(u'quingenti_gig')


    models = {
        u'quingenti.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'quingenti.gig': {
            'Meta': {'object_name': 'Gig'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quingenti.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['quingenti']
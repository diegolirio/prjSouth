# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Telefone.pessoa'
        db.add_column(u'core_telefone', 'pessoa',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Pessoa']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Telefone.pessoa'
        db.delete_column(u'core_telefone', 'pessoa_id')


    models = {
        u'core.cliente': {
            'Meta': {'object_name': 'Cliente', '_ormbases': [u'core.Pessoa']},
            'ie': ('django.db.models.fields.IntegerField', [], {}),
            u'pessoa_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Pessoa']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.endereco': {
            'Meta': {'object_name': 'Endereco'},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logradouro': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.funcionario': {
            'Meta': {'object_name': 'Funcionario', '_ormbases': [u'core.Pessoa']},
            'matricula': ('django.db.models.fields.IntegerField', [], {}),
            u'pessoa_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Pessoa']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.pessoa': {
            'Meta': {'object_name': 'Pessoa'},
            'cpf_cnpj': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Endereco']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.telefone': {
            'Meta': {'object_name': 'Telefone'},
            'ddd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Pessoa']"})
        }
    }

    complete_apps = ['core']
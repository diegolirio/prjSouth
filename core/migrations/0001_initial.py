# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Endereco'
        db.create_table(u'core_endereco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('logradouro', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'core', ['Endereco'])

        # Adding model 'Pessoa'
        db.create_table(u'core_pessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cpf_cnpj', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('endereco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Endereco'])),
        ))
        db.send_create_signal(u'core', ['Pessoa'])

        # Adding model 'Funcionario'
        db.create_table(u'core_funcionario', (
            (u'pessoa_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Pessoa'], unique=True, primary_key=True)),
            ('matricula', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['Funcionario'])

        # Adding model 'Cliente'
        db.create_table(u'core_cliente', (
            (u'pessoa_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Pessoa'], unique=True, primary_key=True)),
            ('ie', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['Cliente'])


    def backwards(self, orm):
        # Deleting model 'Endereco'
        db.delete_table(u'core_endereco')

        # Deleting model 'Pessoa'
        db.delete_table(u'core_pessoa')

        # Deleting model 'Funcionario'
        db.delete_table(u'core_funcionario')

        # Deleting model 'Cliente'
        db.delete_table(u'core_cliente')


    models = {
        u'core.cliente': {
            'Meta': {'object_name': 'Cliente', '_ormbases': [u'core.Pessoa']},
            'ie': ('django.db.models.fields.IntegerField', [], {}),
            u'pessoa_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Pessoa']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.endereco': {
            'Meta': {'object_name': 'Endereco'},
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
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Endereco']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']
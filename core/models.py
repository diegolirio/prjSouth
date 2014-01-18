from django.db import models

class Endereco(models.Model):
	logradouro = models.CharField(max_length=100)
	numero = models.IntegerField(default=0)
	bairro = models.CharField(max_length=50) 
	cidade = models.CharField(max_length=50) 
	estado = models.CharField(max_length=50) 

class Pessoa(models.Model):
	nome = models.CharField(max_length=50)
	cpf_cnpj = models.CharField(max_length=20)
	endereco = models.ForeignKey(Endereco, blank=True)
	
class Telefone(models.Model):
	ddd = models.IntegerField(default=0)
	numero = models.IntegerField(default=0)
	pessoa = models.ForeignKey(Pessoa)	
	
class Funcionario(Pessoa):
	matricula = models.IntegerField()
	#data_admissao = 
	salario = models.DecimalField(max_digits=10, decimal_places=2)
	
class Cliente(Pessoa):
	ie = models.IntegerField()	

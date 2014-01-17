from django.db import models

class Endereco(models.Model):
	logradouro = models.CharField(max_length=100)
	numero = models.IntegerField(default=0)

class Pessoa(models.Model):
	nome = models.CharField(max_length=50)
	cpf_cnpj = models.CharField(max_length=20)
	endereco = models.ForeignKey(Endereco)
	
class Funcionario(Pessoa):
	matricula = models.IntegerField()
	#data_admissao = 
	#salario = 
	
class Cliente(Pessoa):
	ie = models.IntegerField()	

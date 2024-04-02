from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	cod_assessor = models.CharField(max_length=50)
	negocio =  models.CharField(max_length=100)
	cliente = models.CharField(max_length=15)
	data_inicial =  models.CharField(max_length=100)
	data_final =  models.CharField(max_length=50)
	empresa_parceira =  models.CharField(max_length=50)
	anotacoes =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.cod_assessor}")

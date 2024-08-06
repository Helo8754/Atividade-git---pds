from django.db import models

# Create your models here.
class Loja(models.Model):
    nome = models.CharField(max_length= 200)
    endereco = models.CharField(max_length= 100)
    numero = models.IntegerField()
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    cor = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)
    ano = models.IntegerField()

    def __str__(self):
        return self.modelo

class Vendas(models.Model):
    data = models.DateField()
    comprador = models.CharField(max_length=100)
    valor = models.IntegerField()
    carro =models.ForeignKey(Carros, on_delete= models.CASCADE)



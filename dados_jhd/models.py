from django.db import models

class petisco_e_pastel(models.Model):
    nome = models.TextField()
    preco = models.CharField(max_length=10)
    classe= models.CharField(max_length=30)
    def __str__(self):
        return f"{self.nome} cadastrado com sucesso!"
    
class caldo_e_bebidas(models.Model):
    value = models.TextField()
    preco= models.CharField(max_length=10)
    classe = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.value} cadastrado com sucesso!"
    
class pedidos(models.Model):
    numero_mesa = models.CharField(max_length=10)
    pedido = models.TextField()
    visivel = models.BooleanField(default=False)
    is_delete=models.BooleanField(default=False)
    total = models.CharField(max_length=10,default='')

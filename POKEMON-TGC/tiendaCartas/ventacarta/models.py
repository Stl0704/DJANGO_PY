from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.




class Usuario (models.Model):
    nombreu = models.CharField(max_length = 200)
    fNac = models.IntegerField(validators=[MinValueValidator(1920), MaxValueValidator(9999)])
    email = models.EmailField(max_length=254)
    direccion = models.CharField(max_length = 200)




class Carta (models.Model):
    nombre = models.CharField(max_length = 200)
    anio = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    precio = models.DecimalField(max_digits=12,decimal_places=2)
from django.db import models

# Create your models here.







class Municipio(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    codigo = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} - {self.codigo } '

class Linea(models.Model):
    texto = models.CharField(max_length=300, null=True, blank=True)
    mun  = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.texto[0:30]}'
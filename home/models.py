from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Type(models.Model):
    nombre = models.CharField(max_length=10)

    def __unicode__(self):
        return self.nombre

class Place(models.Model):
    typo = models.ForeignKey(Type, on_delete=models.CASCADE)
    nombre_propietario = models.CharField(max_length=50)
    nombre_local = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre_local
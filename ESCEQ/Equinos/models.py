"""
from django.db import models
from django.db.models import Model
from django import forms
from ckeditor.fields import RichTextField


class Raza(models.Model):
    id_raza = models.IntegerField(primary_key=True)
    nom_raza = models.CharField(max_length=255, verbose_name="Nombre raza")
    des_raza = models.CharField(max_length=255, verbose_name="Descripción")
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'

    def __str__(self):
        return "La raza es: %s y su descripción es: %s" % (self.nom_raza, self.des_raza)

"""
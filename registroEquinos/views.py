from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template.loader import get_template
import datetime

meses = ["Seleccione de mes", "Enero", "Febreo", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
         "Octubre", "Noviembre", "Diciembre"]


def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request, "index.html", context=my_dict)


def registroEquino(request):
    f_actual = datetime.datetime.now()
    sexo = ["Seleccione ", "Hembra", "Macho"]

    return render(request, 'registroEquino.html',
                  {"fecha_actual": f_actual, 'meses_del_anio': meses, 'tipo_sexo': sexo})


def regHistoriaClinica(request):

    return render(request, 'historiaClinica.html', {'meses_del_anio': meses})


class Persona(object):
    def __init__(self, mi_nombre, mi_apellido):
        self.nombre = mi_nombre
        self.apellido = mi_apellido


def saludo(request):
    p1 = Persona("Johanna -", "Farfán -")
    fecha_actual = datetime.datetime.now()
    lista_temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    meses = ["Enero", "Febreo", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
             "Noviembre", "Diciembre"]

    return render(request, "C:/Users/JohannaFarfan/Desktop/Tesis/01_proyecto/ESCEQ/ESCEQ/template/miplantilla.html",
                  {'nombre': p1.nombre, 'f_actual': fecha_actual, 'lista': lista_temas, 'los_meses': meses})


def despedida(request):
    return HttpResponse("Chao pescado")

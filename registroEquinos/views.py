from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template.loader import get_template
from registroEquinos.models import Equino

import datetime

meses = ["Seleccione de mes", "Enero", "Febreo", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
         "Octubre", "Noviembre", "Diciembre"]


def busqueda_equinos(request):
    return render(request, "busqueda_equinos.html")


def bus_ser_equ(request):
    # ctrl info form
    if request.GET["txt_caballo"]:
        #mensaje = "Caballo búscado. %r" %request.GET["txt_caballo"]

        texto_caballo = request.GET["txt_caballo"]
        #texto_caballo: object = request.GET["txt_caballo"]
        equinos = Equino.objects.filter(nom_equino__icontains=texto_caballo)
        return render(request, "resultado_equino.html", {"equinos": equinos, "query": equinos})
    else:
        mensaje = "No se ha realizado ninguna búsqueda!"
    return HttpResponse(mensaje)


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

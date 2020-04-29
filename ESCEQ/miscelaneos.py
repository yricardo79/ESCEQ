from django.shortcuts import render


def formatoFecha(request):
    meses = ["Seleccione un mes", "Enero", "Febreo", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
             "Octubre",
             "Noviembre", "Diciembre"]
    return render(request, 'registroEquino.html', {'meses_del_anio': meses})

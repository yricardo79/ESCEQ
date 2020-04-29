from django.shortcuts import render


def formatoFecha(request):
    meses = ["Seleccione un mes", "Enero", "Febreo", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
             "Octubre",
             "Noviembre", "Diciembre"]
    dias_mes = ["Seleccione día", "1", "2", "3", "4"]
    return render(request, 'registroEquino.html', {'meses_del_anio': meses, 'dias_mes': dias_mes})



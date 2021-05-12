from django.core.mail import send_mail
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from registro.forms import formularioContacto


class IndexView(TemplateView):
    template_name = 'index.html'


# Pendientes por revisión
def busqueda_equinos(request):
    return render(request, "busqueda_equinos.html")
    
def bus_ser_equ2(txt_caballo):
    # ctrl info form
    if txt_caballo !="":
        # mensaje = "Caballo búscado. %r" %request.GET["txt_caballo"]
        texto_caballo = txt_caballo
        if len(texto_caballo) > 20:
            return False
        else:
            return True
    else:
        return False

def bus_ser_equ(request):
    # ctrl info form
    if request.GET["txt_caballo"]:
        # mensaje = "Caballo búscado. %r" %request.GET["txt_caballo"]
        texto_caballo = request.GET["txt_caballo"]
        if len(texto_caballo) > 20:
            mensaje = "Busqueda deamasiado larga"
        else:
            # texto_caballo: object = request.GET["txt_caballo"]
            equinos = Equino.objects.filter(nom_equino__icontains=texto_caballo)
            return render(request, "resultado_equino.html", {"equinos": equinos, "query": equinos})
    else:
        mensaje = "No se ha realizado ninguna búsqueda!"
    return HttpResponse(mensaje)


def Contacto(request):
    if request.method == "POST":
        # Guarda la info del formulario
        miFormulario = formularioContacto(request.POST)

        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data
            send_mail(infForm['asunto'], infForm['mensaje'],
                      infForm.get('correo', 'esceq.comentarios.app@gmail.com'),
                      ['esceq.comentarios.app@gmail.com'], )
            return render(request, "gracias.html")
    else:
        # Constr formulario vacio
        miFormulario = formularioContacto()
    return render(request, "formularioContacto.html", {"form": miFormulario})

    # subject = request.POST["txt_asunto"]
    # message = request.POST["txt_mensaje"] + " correo de contacto: " + request.POST["txt_correo"]
    ## Correo de donde viene
    # email_from = settings.EMAIL_HOST_USER
    ## Donde se quiera que vaya la info
    # recipient_list = ["esceq.comentarios.app@gmail.com"]
    # send_mail(subject, message, email_from, recipient_list)
    # return render(request, "gracias.html")
    # return render(request, "contacto.html")


def errorNoFound(request):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'error_no_found.html', {'question': question})

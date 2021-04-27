# from django.shortcuts import render_to_response, RequestContext
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from ESCEQ.Equinos.forms import RazaForm, ComportamientoForm, DisciplinaDeportivaForm, EquDiscForm, EquinoForm
from registro.models import Raza, Comportamiento, Disciplina_Deportiva, Equ_Disc, Equino


# @login_required
# def upload_image_view(request):
#     if request.method == 'POST':
#         form = UploadImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             message = "Image uploaded succesfully!"
#     else:
#         form = UploadImageForm()
#
#     return render_to_response('crear-foto-equ.html', locals(), context_instance=RequestContext(request))
#
#
# def home_view(request):
#     return render_to_response('index.html')


# Tabla Raza
class CrearRaza(CreateView):
    model = Raza
    template_name = 'crear-raza.html'
    form_class = RazaForm
    success_url = reverse_lazy('listar-razas')


class ListarRazas(ListView):
    model = Raza
    template_name = 'listar-razas.html'
    context_object_name = 'razas'
    queryset = Raza.objects.all()


class ActualizarRaza(UpdateView):
    model = Raza
    template_name = 'crear-raza.html'
    form_class = RazaForm
    success_url = reverse_lazy('listar-razas')
    # Para ver la actualización en otra parte usar el metodo def post()


class EliminarRaza(DeleteView):
    model = Raza
    template_name = 'raza_confirm_delete.html'
    success_url = reverse_lazy('listar-razas')


# Tabla Comportamiento
class CrearComportamiento(CreateView):
    model = Comportamiento
    template_name = 'crear-comportamiento.html'
    form_class = ComportamientoForm
    success_url = reverse_lazy('listar-comportamientos')


class ListarComportamientos(ListView):
    model = Comportamiento
    template_name = 'listar-comportamientos.html'
    context_object_name = 'comportamientos'
    queryset = Comportamiento.objects.all()


class ActualizarComportamiento(UpdateView):
    model = Comportamiento
    template_name = 'crear-comportamiento.html'  #
    form_class = ComportamientoForm
    success_url = reverse_lazy('listar-comportamientos')
    # Para ver la actualización en otra parte usar el metodo def post()


class EliminarComportamiento(DeleteView):
    model = Comportamiento
    template_name = 'comportamiento_confirm_delete.html'
    success_url = reverse_lazy('listar-comportamientos')


# Tabla Disciplina_Deportiva
class CrearDisDep(CreateView):
    model = Disciplina_Deportiva
    template_name = 'crear-dis-dep.html'
    form_class = DisciplinaDeportivaForm
    success_url = reverse_lazy('listar-dis-deps')


class ListarDisDeps(ListView):
    model = Disciplina_Deportiva
    template_name = 'listar-dis-deps.html'
    context_object_name = 'disdeps'
    queryset = Disciplina_Deportiva.objects.all()


class ActualizarDisDep(UpdateView):
    model = Disciplina_Deportiva
    template_name = 'crear-dis-dep.html'
    form_class = DisciplinaDeportivaForm
    success_url = reverse_lazy('listar-dis-deps')
    # Para ver la actualización en otra parte usar el metodo def post()


class EliminarDisDep(DeleteView):
    model = Disciplina_Deportiva
    template_name = 'dis-dep_confirm_delete.html'
    success_url = reverse_lazy('listar-dis-deps')


# Tabla Equ_Disc
class CrearEquDisc(CreateView):
    model = Equ_Disc
    template_name = 'crear-equ-dis.html'
    form_class = EquDiscForm
    success_url = reverse_lazy('listar-equ-dis')


class ListarEquDiscs(ListView):
    model = Equ_Disc
    template_name = 'listar-equ-dis.html'
    context_object_name = 'equdiscs'
    queryset = Equ_Disc.objects.all()


class ActualizarEquDisc(UpdateView):
    model = Equ_Disc
    template_name = 'crear-equ-dis.html'
    form_class = EquDiscForm
    success_url = reverse_lazy('listar-equ-dis')
    # Para ver la actualización en otra parte usar el metodo def post()


class EliminarEquDisc(DeleteView):
    model = Equ_Disc
    template_name = 'equ-dis_confirm_delete.html'
    success_url = reverse_lazy('listar-equ-dis')  ############


# Tabla Equino
class CrearEquino(CreateView):
    model = Equino
    template_name = 'crear-equino.html'  # ''
    form_class = EquinoForm
    success_url = reverse_lazy('listar-equinos')


class ListarEquinos(ListView):
    model = Equino
    template_name = 'listar-equinos.html'
    context_object_name = 'equinos'
    queryset = Equino.objects.all()


class ActualizarEquino(UpdateView):
    model = Equino
    template_name = 'crear-equino.html'
    form_class = EquinoForm
    success_url = reverse_lazy('listar-equinos')
    # Para ver la actualización en otra parte usar el metodo def post()


class EliminarEquino(DeleteView):
    model = Equino
    template_name = 'equino_confirm_delete.html'
    success_url = reverse_lazy('listar-equinos')


# # Tabla Foto_Equino
# class CrearFotoEquino(CreateView):
#     model = Foto_Equino
#     form_class = FotoEquinoForm
#     template_name = 'crear-foto-equ.html'
#     success_url = reverse_lazy('listar-fotos-equinos')
#
#
# class ListarFotoEquinos(ListView):
#     model = Foto_Equino
#     template_name = 'listar-fotos-equinos.html'
#     context_object_name = 'fotosequinos'
#     queryset = Foto_Equino.objects.all()
#
#
# class ActualizarFotoEquino(UpdateView):
#     model = Foto_Equino
#     form_class = FotoEquinoForm
#     template_name = 'crear-foto-equ.html'
#     success_url = reverse_lazy('listar-fotos-equinos')
#     # Para ver la actualización en otra parte usar el metodo def post()
#
#
# class EliminarFotoEquino(DeleteView):
#     model = Foto_Equino
#     template_name = 'foto-equino_confirm_delete.html'
#     success_url = reverse_lazy('listar-fotos-equinos')

# NOOOO
# Tabla Foto_Equino
# class CrearRaza(CreateView):
#     model = Foto_Equino
#     template_name = 'crear-raza.html'
#     form_class = FotoEquinoForm
#     success_url = reverse_lazy('listar-razas')
#
#
# class ListarRazas(ListView):
#     model = Raza
#     template_name = 'listar-razas.html'
#     context_object_name = 'razas'
#     queryset = Raza.objects.all()
#
#
# class ActualizarRaza(UpdateView):
#     model = Raza
#     template_name = 'crear-raza.html'
#     form_class = RazaForm
#     success_url = reverse_lazy('listar-razas')
#     # Para ver la actualización en otra parte usar el metodo def post()
#
#
# class EliminarRaza(DeleteView):
#     model = Raza
#     template_name = 'raza_confirm_delete.html'
#     success_url = reverse_lazy('listar-razas')

# def bus_ser_equ(request):
#     # ctrl info form
#     if request.GET["IDENRAZA"]:
#         # mensaje = "Caballo búscado. %r" %request.GET["txt_caballo"]
#         texto_caballo = request.GET["IDENRAZA"]
#         if len(texto_caballo) > 20:
#             mensaje = "Busqueda deamasiado larga"
#         else:
#             # texto_caballo: object = request.GET["txt_caballo"]
#             equinos = Equino.objects.filter(nom_equino__icontains=texto_caballo)
#             return render(request, "prueba.html", {"equinos": equinos, "query": equinos})
#     else:
#         mensaje = "No se ha realizado ninguna búsqueda!"
#     return HttpResponse(mensaje)


# Tabla Disciplina Deportiva
# class CrearDisDep(CreateView):
#     model = Disciplina_Deportiva
#     template_name = 'crear-dis-dep.html'
#     form_class = DisDepForm
#     success_url = reverse_lazy('listar-dis-deps')
#
#
# class ListarDisDeps(ListView):
#     model = Disciplina_Deportiva
#     template_name = 'listar-dis-deps.html'
#     context_object_name = 'disDeps'
#     queryset = Disciplina_Deportiva.objects.all()
#
#
# class ActualizarDisDep(UpdateView):
#     model = Disciplina_Deportiva
#     template_name = 'crear-dis-dep.html'
#     form_class = DisDepForm
#     success_url = reverse_lazy('listar-dis-deps')
#     # Para ver la actualización en otra parte usar el metodo def post()

# class EliminarDisDep(DeleteView):
#     model = Disciplina_Deportiva
#     template_name = 'dis-dep_confirm_delete.html'
#     success_url = reverse_lazy('listar-dis-deps')
#
#
# # Tabla Comp Nutricional
# class CrearComNut(CreateView):
#     model = Comps_Nutricionales
#     template_name = 'crear-com-nut.html'
#     form_class = ComNutForm
#     success_url = reverse_lazy('listar-com-nuts')
#
#
# class ListarComNuts(ListView):
#     model = Comps_Nutricionales
#     template_name = 'listar-com-nuts.html'
#     context_object_name = 'comNuts'
#     queryset = Comps_Nutricionales.objects.all()
#
#
# class ActualizarComNut(UpdateView):
#     model = Comps_Nutricionales
#     template_name = 'crear-com-nut.html'
#     form_class = ComNutForm
#     success_url = reverse_lazy('listar-com-nuts')
#     # Para ver la actualización en otra parte usar el metodo def post()
#
#
# class EliminarComNut(DeleteView):
#     model = Comps_Nutricionales
#     template_name = 'com-nut_confirm_delete.html'
#     success_url = reverse_lazy('listar-com-nuts')

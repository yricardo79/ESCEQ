from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from ESCEQ.veterinarios.forms import VeterinarioForm
from registro.models import Veterinario


class CrearVeterinario(CreateView):
    vet = Veterinario()
    model = Veterinario
    template_name = 'crear-veterinario.html'
    # vet.foto_vet = request.FILES.get('txtFotoVet')
    form_class = VeterinarioForm
    success_url = reverse_lazy('listar-veterinarios')


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
#     return render_to_response('albums/upload.html', locals(), context_instance=RequestContext(request))
#
#
# def home_view(request):
#     return render_to_response('listar-veterinarios.html')

class ListarVeterinarios(ListView):
    model = Veterinario
    template_name = 'listar-veterinarios.html'
    context_object_name = 'veterinarios'
    queryset = Veterinario.objects.all()


class ActualizarVeterinario(UpdateView):
    model = Veterinario
    template_name = 'crear-veterinario.html'
    form_class = VeterinarioForm
    success_url = reverse_lazy('listar-veterinarios')
    # Para ver la actualización en otra parte usar el metodo def post()


class EliminarVeterinario(DeleteView):
    model = Veterinario
    template_name = 'veterinario_confirm_delete.html'
    success_url = reverse_lazy('listar-veterinarios')

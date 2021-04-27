from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from ESCEQ.entornoSalud.forms import CompsNutrionalForm, HistoriaClinicaForm, ConsultaForm, DietaForm
from registro.models import Comps_Nutricional, Historia_Clinica, Consulta, Dieta


# Tabla Comps_Nutrional
class CrearCompsNutricional(CreateView):
    model = Comps_Nutricional
    template_name = 'crear-comps-nut.html'
    form_class = CompsNutrionalForm
    success_url = reverse_lazy('listar-comps-nuts')


class ListarCompsNutricional(ListView):
    model = Comps_Nutricional
    template_name = 'listar-comps-nuts.html'
    context_object_name = 'compsnuts'
    queryset = Comps_Nutricional.objects.all()


class ActualizarCompsNutricional(UpdateView):
    model = Comps_Nutricional
    template_name = 'crear-comps-nut.html'
    form_class = CompsNutrionalForm
    success_url = reverse_lazy('listar-comps-nuts')
    # Para ver la actualización en otra parte usar el metodo def post()


class EliminarCompsNutricional(DeleteView):
    model = Comps_Nutricional
    template_name = 'comps-nuts_confirm_delete.html'
    success_url = reverse_lazy('listar-comps-nuts')


# Historia_Clinica
class CrearHistoriaClinica(CreateView):
    model = Historia_Clinica
    template_name = 'crear-his-cli.html'
    form_class = HistoriaClinicaForm
    success_url = reverse_lazy('listar-his-clis')


class ListarHistoriaClinica(ListView):
    model = Historia_Clinica
    template_name = 'listar-his-clis.html'
    context_object_name = 'hisclis'
    queryset = Historia_Clinica.objects.all()


class ActualizarHistoriaClinica(UpdateView):
    model = Historia_Clinica
    template_name = 'crear-his-cli.html'
    form_class = HistoriaClinicaForm
    success_url = reverse_lazy('listar-his-clis')
    # Para ver la actualización en otra parte usar el metodo def post()


class EliminarHistoriaClinica(DeleteView):
    model = Historia_Clinica
    template_name = 'his-cli_confirm_delete.html'
    success_url = reverse_lazy('listar-his-clis')


# Consulta
class CrearConsulta(CreateView):
    model = Consulta
    template_name = 'crear-consulta.html'
    form_class = ConsultaForm
    success_url = reverse_lazy('listar-consultas')


class ListarConsulta(ListView):
    model = Consulta
    template_name = 'listar-consultas.html'
    context_object_name = 'consultas'
    queryset = Consulta.objects.all()


class ActualizarConsulta(UpdateView):
    model = Consulta
    template_name = 'crear-consulta.html'
    form_class = ConsultaForm
    success_url = reverse_lazy('listar-consultas')
    # Para ver la actualización en otra parte usar el metodo def post()


class EliminarConsulta(DeleteView):
    model = Consulta
    template_name = 'consulta_confirm_delete.html'
    success_url = reverse_lazy('listar-consultas')


# Dieta
class CrearDieta(CreateView):
    model = Dieta
    template_name = 'crear-dieta.html'
    form_class = DietaForm
    success_url = reverse_lazy('listar-dietas')


class ListarDieta(ListView):
    model = Dieta
    template_name = 'listar-dietas.html'
    context_object_name = 'dietas'
    queryset = Dieta.objects.all()


class ActualizarDieta(UpdateView):
    model = Dieta
    template_name = 'crear-dieta.html'
    form_class = DietaForm
    success_url = reverse_lazy('listar-dietas')
    # Para ver la actualización en otra parte usar el metodo def post()


class EliminarDieta(DeleteView):
    model = Dieta
    template_name = 'dieta_confirm_delete.html'
    success_url = reverse_lazy('listar-dietas')

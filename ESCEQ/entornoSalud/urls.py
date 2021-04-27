from django.urls import path

from ESCEQ.entornoSalud.views import CrearCompsNutricional, ListarCompsNutricional, ActualizarCompsNutricional, \
    EliminarCompsNutricional, CrearHistoriaClinica, ListarHistoriaClinica, ActualizarHistoriaClinica, \
    EliminarHistoriaClinica, CrearConsulta, ListarConsulta, ActualizarConsulta, EliminarConsulta, \
    CrearDieta, ListarDieta, ActualizarDieta, EliminarDieta

urlpatterns = [
    # Comps_Nutricional
    path('crear-comps-nut/', CrearCompsNutricional.as_view(), name='crear-comps-nut'),
    path('listar-comps-nuts/', ListarCompsNutricional.as_view(), name='listar-comps-nuts'),
    path('editar-comps-nut/<int:pk>', ActualizarCompsNutricional.as_view(), name='editar-comps-nut'),
    path('eliminar-comps-nut/<int:pk>', EliminarCompsNutricional.as_view(), name='comps-nuts_confirm_delete'),

    # Historia_Clinica
    path('crear-his-cli/', CrearHistoriaClinica.as_view(), name='crear-his-cli'),
    path('listar-his-clis/', ListarHistoriaClinica.as_view(), name='listar-his-clis'),
    path('editar-his-cli/<int:pk>', ActualizarHistoriaClinica.as_view(), name='editar-his-cli'),
    path('eliminar-his-cli/<int:pk>', EliminarHistoriaClinica.as_view(), name='his-cli_confirm_delete'),

    # Consulta
    path('crear-consulta/', CrearConsulta.as_view(), name='crear-consulta'),
    path('listar-consultas/', ListarConsulta.as_view(), name='listar-consultas'),
    path('editar-consulta/<int:pk>', ActualizarConsulta.as_view(), name='editar-consulta'),
    path('eliminar-consulta/<int:pk>', EliminarConsulta.as_view(), name='consulta_confirm_delete'),

    # Dieta
    path('crear-dieta/', CrearDieta.as_view(), name='crear-dieta'),
    path('listar-dietas/', ListarDieta.as_view(), name='listar-dietas'),
    path('editar-dieta/<int:pk>', ActualizarDieta.as_view(), name='editar-dieta'),
    path('eliminar-dieta/<int:pk>', EliminarDieta.as_view(), name='dieta_confirm_delete')
]

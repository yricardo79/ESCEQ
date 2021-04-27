from django.urls import path

from ESCEQ.veterinarios.views import CrearVeterinario, ListarVeterinarios, ActualizarVeterinario, EliminarVeterinario

urlpatterns = [
    path('crear-veterinario/', CrearVeterinario.as_view(), name='crear-veterinario'),
    path('listar-veterinarios/', ListarVeterinarios.as_view(), name='listar-veterinarios'),
    path('editar-veterinario/<int:pk>', ActualizarVeterinario.as_view(), name='editar-veterinario'),
    path('eliminar-veterinario/<int:pk>', EliminarVeterinario.as_view(), name='veterinario_confirm_delete')
]

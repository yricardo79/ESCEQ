from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from ESCEQ.Equinos.views import CrearRaza, ListarRazas, ActualizarRaza, EliminarRaza, \
    CrearComportamiento, ListarComportamientos, ActualizarComportamiento, EliminarComportamiento, \
    CrearDisDep, ListarDisDeps, ActualizarDisDep, EliminarDisDep, \
    CrearEquDisc, ListarEquDiscs, ActualizarEquDisc, EliminarEquDisc, \
    CrearEquino, ListarEquinos, ActualizarEquino, EliminarEquino

# CrearDisDep, ListarDisDeps, ActualizarDisDep, EliminarDisDep, \
# CrearComNut, ListarComNuts, ActualizarComNut, EliminarComNut
urlpatterns = [
    # Raza
    path('crear-raza/', CrearRaza.as_view(), name='crear-raza'),
    path('listar-razas/', ListarRazas.as_view(), name='listar-razas'),
    path('editar-raza/<int:pk>', ActualizarRaza.as_view(), name='editar-raza'),
    path('eliminar-raza/<int:pk>', EliminarRaza.as_view(), name='raza_confirm_delete'),

    # Comportamiento
    path('crear-comportamiento/', CrearComportamiento.as_view(), name='crear-comportamiento'),
    path('listar-comportamientos/', ListarComportamientos.as_view(), name='listar-comportamientos'),
    path('editar-comportamiento/<int:pk>', ActualizarComportamiento.as_view(), name='editar-comportamiento'),
    path('eliminar-comportamiento/<int:pk>', EliminarComportamiento.as_view(), name='comportamiento_confirm_delete'),

    # Disciplina Deportiva
    path('crear-dis-dep/', CrearDisDep.as_view(), name='crear-dis-dep'),
    path('listar-dis-deps/', ListarDisDeps.as_view(), name='listar-dis-deps'),
    path('editar-dis-dep/<int:pk>', ActualizarDisDep.as_view(), name='editar-dis-dep'),
    path('eliminar-dis-dep/<int:pk>', EliminarDisDep.as_view(), name='dis-dep_confirm_delete'),

    # Equ_Disc
    path('crear-equ-dis/', CrearEquDisc.as_view(), name='crear-equ-dis'),
    path('listar-equ-dis/', ListarEquDiscs.as_view(), name='listar-equ-dis'),
    path('editar-equ-dis/<int:pk>', ActualizarEquDisc.as_view(), name='editar-equ-dis'),
    path('eliminar-equ-dis/<int:pk>', EliminarEquDisc.as_view(), name='equ-dis_confirm_delete'),

    # Equino
    path('crear-equino/', CrearEquino.as_view(), name='crear-equino'),
    path('listar-equinos/', ListarEquinos.as_view(), name='listar-equinos'),
    path('editar-equino/<int:pk>', ActualizarEquino.as_view(), name='editar-equino'),
    path('eliminar-equino/<int:pk>', EliminarEquino.as_view(), name='equino_confirm_delete')

    # Foto_Equino
    # path('upload_image_view/', CrearEquino.as_view(), name='upload_image_view'),

    # Foto_Equino
    # path('crear-foto-equino/', CrearFotoEquino.as_view(), name='crear-foto-equino'),
    # path('listar-fotos-equinos/', ListarFotoEquinos.as_view(), name='listar-fotos-equinos'),
    # path('editar-foto-equino/<int:pk>', ActualizarFotoEquino.as_view(), name='editar-foto-equino'),
    # path('eliminar-foto-equino/<int:pk>', EliminarFotoEquino.as_view(), name='foto-equino_confirm_delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

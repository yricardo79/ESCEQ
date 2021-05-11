from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import CrearVars

urlpatterns = [
    # path('calcular-vars-yo/', CrearVarsYo.as_view(), name='calcular-vars-yo'),
    path('calcular-vars/', CrearVars.as_view(), name='calcular-vars'),
    path('puntajepredecido/', TemplateView.as_view(template_name='puntajepredecido.html'), name='puntajepredecido'),
    path('cargue-archivo/', TemplateView.as_view(template_name='cargue-archivo.html'), name='cargue-archivo'),
    path('capturaExcepciones/', TemplateView.as_view(template_name='capturaExcepciones.html'),
         name='capturaExcepciones'),
    path('list/', views.list, name='list'),
    path('validar_extension/', views.validar_extension, name='validar_extension'),
    path('mostrargraficaEntrenamiento/', TemplateView.as_view(template_name='mostrargraficaEntrenamiento.html'),
         name='mostrargraficaEntrenamiento'),
    path('mostrarKNN/', TemplateView.as_view(template_name='mostrarKNN.html'), name='mostrarKNN'),
    path('mostrargraficaEquinos/', TemplateView.as_view(template_name='mostrargraficaEquinos.html'),
         name='mostrargraficaEquinos'),
    path('mostrargraficaMayorP/', TemplateView.as_view(template_name='mostrargraficaMayorP.html'),
         name='mostrargraficaMayorP'),
    path('graficaEntrenamiento/', views.graficaEntrenamiento, name='graficaEntrenamiento'),
    path('graficaEquinosPuntaje/', views.graficaEquinosPuntaje, name='graficaEquinosPuntaje'),
    path('graficaMaxPuntajes/', views.graficaMaxPuntajes, name='graficaMaxPuntajes'),
    path('predecir/', views.predecir, name='predecir'),
    path('exportar/', views.exportar, name='exportar'),
    path('graficaKNN/', views.graficaKNN, name='graficaKNN'),

]

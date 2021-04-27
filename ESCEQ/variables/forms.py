from django import forms

from registro.models import Variables, Equino
from .Validador import *

GRADO_CLAUDICACION = ['0', '1', '2', '3']

class VarsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['chip'].widget.attrs['autofocus'] = True
        self.fields['grado_claudi'].validators.append(variables_validation)

    class Meta:
        model = Variables
        fields = [
            'chip', 'claudicacion', 'grado_claudi', 'presencia_sangre', 'olleres', 'boca', 'heridas_sangrantes',
            'evidencia_fat_sud',
            'grano', 'forraje', 'suplemento', 'sup_oral', 'sup_intravenoso', 'dieta_veces_dia',
            'dieta_horarios', 'calentamiento_previo', 'hora_calentamiento', 'minuto_calentamiento',
            'trabajo_cantidad_horas', 'trabajo_cantidad_diaria', 'trabajo_cantidad_semanal', 'trabajo_potrero',
            'trabajo_caminador', 'tiempo_pot_cam_horas', 'tiempo_pot_cam_mins'
        ]
        labels = {
            'chip': 'Chip Equino',
            'claudicacion': 'La claudicación del caballo',
            'grado_claudi ': 'Grado de claudicación',
            'presencia_sangre': 'Presencia en sangre',
            'olleres': 'Olleres',
            'boca': 'Boca',
            'heridas_sangrantes': 'Heridas sangrantes',
            'evidencia_fat_sud': 'Evidencia fatiga o sudoración',
            'grano': 'Grano Cantidad (kilogramos)',
            'forraje': 'Forraje Cantidad (kilogramos)',
            'suplemento': 'Sumplemento',
            'sup_oral': 'Suplemento oral',
            'sup_intravenoso': 'Suplemento intravenoso',
            'dieta_veces_dia': 'Dieta veces al dia',
            'dieta_horarios': 'Dieta horarios',
            'calentamiento_previo': 'Calentamiento previo',
            'hora_calentamiento': 'Horas calentamiento',
            'minuto_calentamiento': 'Minutos calentamiento',
            'trabajo_cantidad_horas': 'Trabajo cantidad de horas',
            'trabajo_cantidad_diaria': 'Trabajo cantidad diario',
            'trabajo_cantidad_semanal': 'Trabajo cantidad semanal',
            'trabajo_potrero': 'Trabajo potrero',
            'trabajo_caminador': 'Trabajo caminado',
            'tiempo_pot_cam_horas': 'Tiempo potrero o caminador horas',
            'tiempo_pot_cam_mins': 'Tiempo potrero o caminador minutos',
        }
        widgets = {
            'chip ': forms.Select(
                attrs={
                    'id': 'chip'
                }
            ),
            'claudicacion': forms.Select(
                attrs={
                    'id': 'claudicacion'
                }
            ),
            'grado_claudi': forms.TextInput(
                attrs={
                    'id': 'grado_claudi'
                }
            ),
            'presencia_sangre': forms.Select(
                attrs={
                    'id': 'presencia_sangre'
                }
            ),
            'olleres': forms.Select(
                attrs={
                    'id': 'olleres'
                }
            ),
            'boca': forms.Select(
                attrs={
                    'id': 'boca'
                }

            ),
            'heridas_sangrantes': forms.Select(
                attrs={
                    'id': 'heridas_sangrantes'
                }

            ),
            'evidencia_fat_sud': forms.Select(
                attrs={
                    'id': 'evidencia_fat_sud'
                }

            ),
            'grano': forms.TextInput(
                attrs={
                    'id': 'grano'
                }

            ),
            'forraje': forms.TextInput(
                attrs={
                    'id': 'forraje'
                }

            ),
            'suplemento': forms.Select(
                attrs={
                    'id': 'suplemento'
                }

            ),
            'sup_oral': forms.Select(
                attrs={
                    'id': 'sup_oral'
                }

            ),
            'sup_intravenoso': forms.Select(
                attrs={
                    'id': 'sup_intravenoso'
                }

            ),
            'dieta_veces_dia': forms.TextInput(
                attrs={
                    'id': 'dieta_veces_dia'
                }

            ),
            'dieta_horarios': forms.TextInput(
                attrs={
                    'id': 'dieta_horarios'
                }

            ),
            'calentamiento_previo': forms.Select(
                attrs={
                    'id': 'calentamiento_previo'
                }

            ),
            'hora_calentamiento': forms.TextInput(
                attrs={
                    'id': 'hora_calentamiento'
                }

            ),
            'minuto_calentamiento': forms.TextInput(
                attrs={
                    'id': 'minuto_calentamiento'
                }

            ),
            'trabajo_cantidad_horas': forms.TextInput(
                attrs={
                    'id': 'trabajo_cantidad_horas'
                }

            ),
            'trabajo_cantidad_diaria': forms.TextInput(
                attrs={
                    'id': 'trabajo_cantidad_diaria'
                }

            ),
            'trabajo_cantidad_semanal': forms.TextInput(
                attrs={
                    'id': 'trabajo_cantidad_semanal'
                }

            ),
            'trabajo_cantidad_semanal': forms.TextInput(
                attrs={
                    'id': 'trabajo_cantidad_semanal'
                }

            ),
            'trabajo_potrero': forms.Select(
                attrs={
                    'id': 'trabajo_potrero'
                }

            ),
            'trabajo_caminador': forms.Select(
                attrs={
                    'id': 'trabajo_caminador'
                }

            ),
            'tiempo_pot_cam_horas': forms.TextInput(
                attrs={
                    'id': 'tiempo_pot_cam_horas'
                }

            ),
            'tiempo_pot_cam_mins': forms.TextInput(
                attrs={
                    'id': 'tiempo_pot_cam_mins'
                }

            ),

        }

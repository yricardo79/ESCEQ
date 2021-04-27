from django import forms

from registro.models import Veterinario


class VeterinarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['cedula'].widget.attrs['autofocus'] = True

    class Meta:
        model = Veterinario
        fields = ['cedula', 'nombres_veterinario', 'apellidos_veterinario', 'fecha_nac_veterinario',
                  'correo_veterinario']  # , 'foto_vet'
        labels = {
            'cedula': 'Cédula veterinario',
            'nombres_veterinario': 'Nombres del veterinario',
            'apellidos_veterinario': 'Apellidos del veterinario',
            'correo_veterinario': 'Correo del veterinario',
            'fecha_nac_veterinario': 'Fecha nacimiento del veterinario',
            # 'foto_vet': 'Foto',
        }
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese cédula',
                    'id': 'cedula'
                }
            ),
            'nombres_veterinario': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese los nombres',
                    'id': 'nombres_veterinario'
                }
            ),
            'apellidos_veterinario': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese los apellidos',
                    'id': 'apellidos_veterinario'
                }
            ),
            'correo_veterinario': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese correo del veterinario',
                    'id': 'correo_veterinario'
                }
            ),
            'fecha_nac_veterinario': forms.DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'date', 'placeholder': '__/__/____'}
            ),
            # 'foto_vet': forms.ImageField(
            #     # attrs={'type': 'hidden'}
            # ),

            # 'foto_vet': forms.ImageField(
            #     disabled=True
            #     # widget=CustomClearableFileInput
            #     # attrs={'id': 'foto_vet'}
            #
            # ),
        }

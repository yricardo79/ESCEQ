from django import forms

from registro.models import Raza, Comportamiento, Disciplina_Deportiva, Equ_Disc, Equino  # , Foto_Equino


# class UploadImageForm(forms.ModelForm):
#     class Meta:
#         model = Foto_Equino  # AlbumImage
#         fields = ['equino', 'imagen']


# Foto_Equino  # , Comps_Nutricionales
# class FotoEquinoForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for form in self.visible_fields():
#             form.field.widget.attrs['class'] = 'form-control'
#         self.fields['equino'].widget.attrs['autofocus'] = True
#
#     class Meta:
#         model = Foto_Equino
#         fields = ['equino', 'foto']
#         labels = {
#             'equino': 'Equino',
#             'foto': 'Foto del equino',
#         }
#         widgets = {
#             'equino': forms.Select(
#                 attrs={
#                     'id': 'equino'
#                 }
#             ),
#         }


class RazaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['nom_raza'].widget.attrs['autofocus'] = True

    class Meta:
        model = Raza
        fields = ['nom_raza', 'des_raza']
        labels = {
            # 'id_raza': 'Identificador de raza',
            'nom_raza': 'Nombre de la raza',
            'des_raza': 'Descripción de la raza',
        }
        widgets = {
            # 'id_raza': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Ingrese el id de la raza',
            #         'id': 'id_raza',
            #     }
            # ),
            'nom_raza': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre de la raza',
                    'id': 'nom_raza'
                }
            ),
            'des_raza': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese descripción de la raza',
                    'id': 'des_raza'
                }
            ),
        }


class ComportamientoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['nombre_com'].widget.attrs['autofocus'] = True

    class Meta:
        model = Comportamiento
        fields = ['nombre_com', 'descripcion_com']  #
        labels = {
            # 'id_comp': 'Identificador de comportamiento',
            'nombre_com': 'Nombre comportamiento',
            'descripcion_com': 'Descripción comportamiento',
        }
        widgets = {
            # 'id_comp': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Ingrese el id de comportamiento',
            #         'id': 'id_comp'
            #     }
            # ),
            'nombre_com': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre comportamiento',
                    'id': 'nombre_com'
                }
            ),
            'descripcion_com': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese descripción comportamiento',
                    'id': 'descripcion_com'
                }
            ),
        }


class DisciplinaDeportivaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['nombre_dis_dep'].widget.attrs['autofocus'] = True

    class Meta:
        model = Disciplina_Deportiva
        fields = ['nombre_dis_dep', 'descripcion_dis_dep']
        labels = {
            # 'id_dis_dep': 'Iden disciplina deportiva',
            'nombre_dis_dep': 'Nombre disciplina deportiva',
            'descripcion_dis_dep': 'Descripción disciplina deportiva',
        }
        widgets = {
            # 'id_dis_dep': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Ingrese iden disciplina deportiva',
            #         'id': 'id_dis_dep'
            #     }
            # ),
            'nombre_dis_dep': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre disciplina deportiva',
                    'id': 'nombre_dis_dep'
                }
            ),
            'descripcion_dis_dep': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese descripción disciplina deportiva',
                    'id': 'descripcion_dis_dep'
                }
            ),
        }


class EquDiscForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['disciplina_id'].widget.attrs['autofocus'] = True

    class Meta:
        model = Equ_Disc
        fields = ['disciplina_id', 'exigencia']
        labels = {
            # 'chip_equ_disc': 'Chip equino disciplina',
            'disciplina_id': 'Id disciplina',
            'exigencia': 'Exigencia',
        }

        widgets = {
            # 'chip_equ_disc': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Ingrese chip equino disciplina',
            #         'id': 'chip_equ_disc'
            #     }
            # ),
            'disciplina_id': forms.Select(
                attrs={
                    'id': 'disciplina_id'
                }
            ),
            'exigencia': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese Exigencia',
                    'id': 'exigencia'
                }
            ),
        }


class EquinoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['chip'].widget.attrs['autofocus'] = True

    class Meta:
        model = Equino
        fields = ['chip', 'nom_equino', 'fec_nacimiento', 'adv_manejo', 'sexo', 'color',
                  'raza', 'comportamiento', 'disciplia']  # , 'foto_equ'
        labels = {
            'chip': 'Chip del equino',
            'nom_equino': 'Nombre del equino',
            'fec_nacimiento': 'Fecha de nacimiento',
            'adv_manejo': 'adv_manejo',
            'sexo': 'sexo',
            'color': 'color',
            'raza': 'Identificador de raza',
            'comportamiento': 'Comportamiento',
            'disciplia': 'Disciplina',
            # 'foto_equ': 'Foto'
        }
        widgets = {
            'chip': forms.TextInput(
                attrs={
                    'placeholder': '',
                    'id': 'chip'
                }
            ),
            'nom_equino': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre',
                    'id': 'nom_equino'
                }
            ),
            'fec_nacimiento': forms.DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'date', 'placeholder': '__/__/____'}
            ),
            'adv_manejo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese adv_manejo',
                    'id': 'adv_manejo'
                }
            ),

            'sexo': forms.Select(
                attrs={
                    'id': 'sexo'
                }
            ),

            'color': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el nomre',
                    'id': 'color'
                }
            ),
            'raza': forms.Select(
                attrs={
                    'id': 'raza'
                }
            ),
            'comportamiento': forms.Select(
                attrs={
                    'id': 'comportamiento'
                }
            ),
            'disciplia': forms.Select(
                attrs={
                    'id': 'disciplia'
                }
            ),
        }

# class FotoEquinoForm():
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for form in self.visible_fields():
#             form.field.widget.attrs['class'] = 'form-control'
#         self.fields['equino'].widget.attrs['autofocus'] = True
#
#     class Meta:
#         model = Foto_Equino
#         fields = ['equino', 'image']
# labels = {
#     'nom_raza': 'Nombre de la raza',
#     'des_raza': 'Descripción de la raza',
# }

#
#
# class ComNutForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for form in self.visible_fields():
#             form.field.widget.attrs['class'] = 'form-control'
#         self.fields['id_comp'].widget.attrs['autofocus'] = True
#
#     class Meta:
#         model = Comps_Nutricionales
#         fields = ['id_comp', 'comp_nutricional', 'tipo_componente', 'observaciones']
#         labels = {
#             'id_comp': 'Iden componente',
#             'comp_nutricional': 'Componente nutricional',
#             'tipo_componente': 'Tipo de componete',
#             'observaciones': 'Observaciones',
#         }
#         widgets = {
#             'id_comp': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese iden componente',
#                     'id': 'id_comp'
#                 }
#             ),
#             'comp_nutricional': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese componente nutriconal',
#                     'id': 'comp_nutricional'
#                 }
#             ),
#             'tipo_componente': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese tipo componente',
#                     'id': 'tipo_componente'
#                 }
#             ),
#             'observaciones': forms.Textarea(
#                 attrs={
#                     'placeholder': 'Ingrese observaciones',
#                     'id': 'observaciones'
#                 }
#             ),
#         }

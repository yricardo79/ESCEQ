from django import forms

from registro.models import Comps_Nutricional, Historia_Clinica, Consulta, Dieta


class CompsNutrionalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['comp_nutricional'].widget.attrs['autofocus'] = True

    class Meta:
        model = Comps_Nutricional
        fields = ['comp_nutricional', 'tipo_componente', 'observaciones']
        labels = {
            'comp_nutricional': 'Comp nutricional',
            'tipo_componente': 'Tipo de componente',
            'observaciones': 'Observaciones',
        }
        widgets = {
            'comp_nutricional': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre componente',
                    'id': 'comp_nutricional',
                }
            ),
            'tipo_componente': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese tipo de componente',
                    'id': 'tipo_componente'
                }
            ),
            'observaciones': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese observaciones',
                    'id': 'observaciones'
                }
            ),
        }


class HistoriaClinicaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['equino_chip'].widget.attrs['autofocus'] = True

    class Meta:
        model = Historia_Clinica
        fields = ['equino_chip', 'cedula_vet', 'fecha_apertura', 'estado', 'observaciones']
        labels = {
            'equino_chip': 'Chip equino',
            'cedula_vet': 'Cédula veterinario',
            'fecha_apertura': 'fecha_apertura',
            'estado': 'Estado',
            'observaciones': 'Observaciones',
        }
        widgets = {
            'equino_chip': forms.Select(
                attrs={
                    'id': 'equino_chip'
                }
            ),
            'cedula_vet': forms.Select(
                attrs={
                    'id': 'cedula_vet'
                }
            ),
            'fecha_apertura': forms.DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'date', 'placeholder': '__/__/____'}
            ),
            'estado': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese estado',
                    'id': 'estado'
                }
            ),
            'observaciones': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese observaciones',
                    'id': 'observaciones'
                }
            ),
        }


class ConsultaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['chip_equino'].widget.attrs['autofocus'] = True

    class Meta:
        model = Consulta
        fields = ['chip_equino', 'fecha', 'historia_clinica', 'frec_cardiaca', 'frec_respiratoria', 'pulso',
                  'temperatura', 'est_hidratacion', 'porc_deshidrat', 'peso', 'conjuntival', 'oral',
                  'vulva_prepucio',
                  'rectal', 'ojos', 'oidos', 'nod_linfaticos']
        labels = {
            'chip_equino': 'chip_equino',
            'fecha': 'fecha',
            'historia_clinica': 'historia_clinica',
            'frec_cardiaca': 'frec_cardiaca',
            'frec_respiratoria': 'frec_respiratoria',
            'pulso': 'pulso',
            'temperatura': 'temperatura',
            'est_hidratacion': 'est_hidratacion',
            'porc_deshidrat': 'porc_deshidrat',
            'peso': 'peso',
            'conjuntival': 'conjuntival',
            'oral': 'oral',
            'vulva_prepucio': 'vulva_prepucio',
            'rectal': 'rectal',
            'ojos': 'ojos',
            'oidos': 'oidos',
            'nod_linfaticos': 'nod_linfaticos',
        }
        widgets = {
            'chip_equino': forms.Select(
                attrs={
                    'id': 'chip_equino'
                }
            ),
            'fecha': forms.DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'date', 'placeholder': '__/__/____'}
            ),
            'historia_clinica': forms.Select(
                attrs={
                    'id': 'historia_clinica'
                }
            ),
            'frec_cardiaca': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese frec cardiaca',
                    'id': 'frec_cardiaca'
                }
            ),
            'frec_respiratoria': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese frec respiratoria',
                    'id': 'frec_respiratoria'
                }
            ),
            'pulso': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese pulso',
                    'id': 'pulso'
                }
            ),
            'temperatura': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese temperatura',
                    'id': 'temperatura'
                }
            ),
            'est_hidratacion': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese est hidratacion',
                    'id': 'est_hidratacion'
                }
            ),
            'porc_deshidrat': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese porc_deshidrat',
                    'id': 'porc_deshidrat'
                }
            ),
            'peso': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese peso',
                    'id': 'peso'
                }
            ),
            'conjuntival': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese conjuntival',
                    'id': 'conjuntival'
                }
            ),
            'oral': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese medición oral',
                    'id': 'oral'
                }
            ),
            'vulva_prepucio': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese vulva ó prepucio',
                    'id': 'vulva_prepucio'
                }
            ),
            'rectal': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese medición rectal',
                    'id': 'rectal'
                }
            ),
            'ojos': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese medición ojos',
                    'id': 'ojos'
                }
            ),
            'oidos': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese medición oidos',
                    'id': 'oidos'
                }
            ),
            'nod_linfaticos': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese nod linfaticos',
                    'id': 'nod_linfaticos'
                }
            ),
        }


class DietaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['nombre_dieta'].widget.attrs['autofocus'] = True

    class Meta:
        model = Dieta
        #
        fields = ['chip_equino', 'nombre_dieta', 'id_fecha', 'comps_nutricionales_id', 'veterinario_cedula', 'estado',
                  'id_des_conc', 'cant_des_conc', 'id_alm_con', 'cant_alm_conc', 'id_com_conc', 'cant_com_conc',
                  'id_des_forraje', 'cant_des_forraje', 'id_alm_forraje', 'cant_alm_forraje', 'id_des_suple',
                  'cant_des_suple', 'id_alm_suple', 'cant_alm_suple', 'id_com_suple', 'cant_com_suple', 'hora_des_conc',
                  'hora_des_forraje', 'hora_des_suple', 'hora_alm_suple', 'hora_alm_forraje', 'hora_alm_conc',
                  'hora_com_suple', 'hora_com_forraje']
        labels = {
            'chip_equino': 'chip_equino',
            'nombre_dieta': 'nombre_dieta',
            'id_fecha': 'id_fecha',
            'comps_nutricionales_id': 'comps_nutricionales_id',
            'veterinario_cedula': 'veterinario_cedula',
            'estado': 'estado',
            'id_des_conc': 'id_des_conc',
            'cant_des_conc': 'cant_des_conc',
            'id_alm_con': 'id_alm_con',
            'cant_alm_conc': 'cant_alm_conc',
            'id_com_conc': 'id_com_conc',
            'cant_com_conc': 'cant_com_conc',
            'id_des_forraje': 'id_des_forraje',
            'cant_des_forraje': 'cant_des_forraje',
            'id_alm_forraje': 'id_alm_forraje',
            'cant_alm_forraje': 'cant_alm_forraje',
            'id_des_suple': 'id_des_suple',
            'cant_des_suple': 'cant_des_suple',
            'id_alm_suple': 'id_alm_suple',
            'cant_alm_suple': 'cant_alm_suple',
            'id_com_suple': 'id_com_suple',
            'cant_com_suple': 'cant_com_suple',
            'hora_des_conc': 'hora_des_conc',
            'hora_des_forraje': 'hora_des_forraje',
            'hora_des_suple': 'hora_des_suple',
            'hora_alm_suple': 'hora_alm_suple',
            'hora_alm_forraje': 'hora_alm_forraje',
            'hora_alm_conc': 'hora_alm_conc',
            'hora_com_suple': 'hora_com_suple',
            'hora_com_forraje': 'hora_com_forraje',
        }
        widgets = {
            'chip_equino': forms.Select(
                attrs={
                    'id': 'chip_equino'
                }
            ),
            'nombre_dieta': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre_dieta',
                    'id': 'nombre_dieta'
                }
            ),
            'id_fecha': forms.DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'date', 'placeholder': '__/__/____'}
            ),
            'comps_nutricionales_id': forms.Select(
                attrs={
                    'id': 'comps_nutricionales_id'
                }
            ),
            'veterinario_cedula': forms.Select(
                attrs={
                    'id': 'veterinario_cedula'
                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese estado',
                    'id': 'estado'
                }
            ),
            'id_des_conc': forms.NumberInput(),
            'cant_des_conc': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese cant_des_conc',
                    'id': 'cant_des_conc'
                }
            ),
            'id_alm_con': forms.NumberInput(),
            'cant_alm_conc': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese cant_alm_conc',
                    'id': 'cant_alm_conc'
                }
            ),
            'id_com_conc': forms.NumberInput(),
            'cant_com_conc': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese cant_com_conc',
                    'id': 'cant_com_conc'
                }
            ),
            'id_des_forraje': forms.NumberInput(),
            'cant_des_forraje': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese cant_des_forraje ',
                    'id': 'cant_des_forraje '
                }
            ),
            'id_alm_forraje': forms.NumberInput(),
            'cant_alm_forraje': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese cant_alm_forraje',
                    'id': 'cant_alm_forraje'
                }
            ),
            'id_des_suple': forms.NumberInput(),
            'cant_des_suple': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese cant_des_suple',
                    'id': 'cant_des_suple'
                }
            ),
            'id_alm_suple': forms.NumberInput(),
            'cant_alm_suple': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese cant_alm_suple',
                    'id': 'cant_alm_suple'
                }
            ),
            'id_com_suple': forms.NumberInput(),
            'cant_com_suple': forms.NumberInput(),
            'hora_des_conc': forms.TimeInput(attrs={'type': 'time'}),
            'hora_des_forraje': forms.TimeInput(attrs={'type': 'time'}),
            'hora_des_suple': forms.TimeInput(attrs={'type': 'time'}),
            'hora_alm_suple': forms.TimeInput(attrs={'type': 'time'}),
            'hora_alm_forraje': forms.TimeInput(attrs={'type': 'time'}),
            'hora_alm_conc': forms.TimeInput(attrs={'type': 'time'}),
            'hora_com_suple': forms.TimeInput(attrs={'type': 'time'}),
            'hora_com_forraje': forms.TimeInput(attrs={'type': 'time'}),
        }
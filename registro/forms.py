from django import forms


class formularioContacto(forms.Form):
    # Especificación de campos
    asunto = forms.CharField()
    correo = forms.EmailField()
    mensaje = forms.CharField()

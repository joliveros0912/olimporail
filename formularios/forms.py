from django import forms
from django.http import HttpResponse
from apia.models import cliente, tipo_documento, empleados, tipo_empleado
from django.contrib.auth import authenticate, login




class registrocliente(forms.ModelForm):
    
    tipo_doc = forms.ModelChoiceField(queryset=tipo_documento.objects.all(), required=True, label="Tipo de Documento")
    contrasenaaC = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    def __init__(self, *args, **kwargs):
        super(registrocliente, self).__init__(*args, **kwargs)
        self.fields['tipo_doc'].label_from_instance = lambda obj: "%s" % obj.tipo_documento

    class Meta:
        model = cliente
        fields = ['tipo_doc', 'numero_doc', 'correo', 'nombre', 'numero_contacto', 'contrasenaaC']


class loginclientes(forms.Form):
    tipo_usuario = forms.ModelChoiceField(queryset=tipo_empleado.objects.all(), label="Tipo de Usuario")
    def __init__(self, *args, **kwargs):
        super(loginclientes, self).__init__(*args, **kwargs)
        self.fields['tipo_usuario'].label_from_instance = lambda obj: "%s" % obj.tipo_empleado

    numero_doc = forms.CharField(required=True)
    contrasenaaC = forms.CharField(widget=forms.PasswordInput, required=True)

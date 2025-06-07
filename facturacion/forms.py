from django import forms
from .models import Cliente, UsuarioRegistro

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'class': 'form-control',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'form-control',
        })
    )

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class UsuarioRegistroForm(forms.ModelForm):  # FUERA de ClienteForm
    class Meta:
        model = UsuarioRegistro
        fields = '__all__'
        widgets = {
            'tipo_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento_1': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'regimen': forms.TextInput(attrs={'class': 'form-control'}),
            'responsabilidad': forms.TextInput(attrs={'class': 'form-control'}),
            'obligaciones_dian': forms.TextInput(attrs={'class': 'form-control'}),
        }

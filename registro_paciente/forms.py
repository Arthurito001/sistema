from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Registro,Pruebas
from django.forms import ModelChoiceField
from django.forms import modelformset_factory

class RegistroDosForm(forms.ModelForm):
    necesita_factura = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    #nombre_prueba = forms.CharField(max_length=100, label='Nombre de la prueba')
    #opciones_pruebas = forms.ModelChoiceField(queryset=Pruebas.objects.none(), required=False, empty_label="Selecciona una prueba") 
   
    class Meta:
      model = Registro
      fields = "__all__"

class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))   
    
class ResultadosForm(forms.Form):
    busqueda = forms.CharField(label='Búsqueda')
    #informacion_adicional = forms.CharField(max_length=200, required=False)
    #informacion_adicional = forms.CharField(label='Información Adicional', required=False, widget=forms.Textarea)  # Campo para capturar la información adicional

class InformacionAdicionalForm(forms.Form):
   informacion_adicional = forms.CharField(widget=forms.Textarea)

class CargaArchivosForm(forms.Form):
   file = forms.FileField()

class PruebasForm(forms.ModelForm):
   search_query = forms.CharField(label='Ingrese prueba ') #variable de busqueda de texto completo
   nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'search-field'}))
 
   class Meta:
       model = Pruebas # Aquí es donde se define la clase del modelo
       fields = ['nombre','costo']

class BusquedaForm(forms.Form):
 busqueda = forms.CharField(max_length=100)

PruebasFormSet = forms.modelformset_factory(Pruebas, form=PruebasForm, extra=4)

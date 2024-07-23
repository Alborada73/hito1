from django import forms  
from .models import Comuna, Region 

class InmuebleForm(forms.Form):
    TIPO_INMUEBLE_CHOICES = (
        ('1', 'Casa'),
        ('2', 'Departamento'),
        ('3', 'Parcela')
    )
    comunas = Comuna.objects.all()
    regiones = Region.objects.all()
    nombre = forms.CharField(max_length=50)
    descripcion = forms.TextField()
    m2_construidos = forms.FloatField()
    m2_terreno = forms.FloatField()
    num_estacionamientos =forms.IntegerField()
    num_habitaciones = forms.IntegerField()
    num_banios = forms.IntegerField()
    direccion = forms.CharField(max_length=50)
    precio_mensual = forms.FloatField()
    comuna = forms.ChoiceField(choices=comunas)
    region = forms.ChoiceField(choices=regiones)
    tipo_inmueble = forms.ChoiceField(choices=TIPO_INMUEBLE_CHOICES)
  
   
from django import forms
from .models import Anime
from datetime import datetime

class RegistarAnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['nombre', 'autor', 'descripcion', 'anio_lanzamiento', 'precio', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': "Ingresa el nombre del anime"
            }),
            'descripcion': forms.Textarea(attrs={
                'rows': 5
            })
        }
        
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip() 
        if len(nombre) < 5:
            raise forms.ValidationError('El nombre tiene que ser minimo 5 caracteres')
        return nombre
    
    def clean_anio_lanzamiento(self):
        anio_actual = datetime.now().year
        anio_lanzamiento = self.cleaned_data['anio_lanzamiento']
        
        if anio_lanzamiento > anio_actual:
            raise forms.ValidationError('El anio de lanzamiento no puede ser mayor al anio actual')
        return anio_lanzamiento
    
    def clean_precio(self):
        precio = self.cleaned_data['precio']
        
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser menor a 0')
        return precio
    
    

    
    

        
        
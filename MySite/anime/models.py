from django.db import models



# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f'{self.nombre}'


class Anime(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    anio_lanzamiento = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagen = models.ImageField(upload_to='animes/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'
        
    def __str__(self):
        return f'{self.nombre}'
    
    
    
    
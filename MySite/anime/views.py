from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistarAnimeForm
from .models import Anime
from django.contrib import messages
from decimal import Decimal

# Create your views here.
def home(request):
    return render(request, 'home.html')


def agregar_anime(request):
    if request.method == 'POST':
        form = RegistarAnimeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            precio = data['precio'] * Decimal(1.50)
            anime = Anime(
                nombre = data['nombre'],
                descripcion = data['descripcion'],
                precio =  precio ,
                anio_lanzamiento = data['anio_lanzamiento'],
                autor = data['autor'],
                imagen = data['imagen']
            )
            anime.save()
            messages.success(request, 'Anime guardado correctamente')
            print('todo salio bien :v')
            return redirect('anime:listar')
        print(form.errors)
        messages.error(request, 'Revisa los campos del formulario')
    else:
        form = RegistarAnimeForm()
        
    contexto = {'form': form}
    return render(request, 'crear.html', contexto)


def detalle_anime(request, pk):
    try:
        anime = get_object_or_404(Anime, pk=pk)
        return render(request, 'detalle.html', {'anime':anime})
    except Exception as e:
        print(str(e))
        
        
def listar_animes(request):
    animes = Anime.objects.all()
    return render(request, 'listar.html', {'animes':animes})


def update_anime(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        form = RegistarAnimeForm(request.POST, request.FILES, instance=anime)
        if form.is_valid():
            form.save()
            messages.success(request, 'Anime actualizado')
            return redirect('anime:listar')
        messages.error(request, 'Error revisa los campos del formulario')
        
    else:
        form = RegistarAnimeForm(instance=anime)
        
    return render(request, 'crear.html', {'form':form})


def delete_anime(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        anime.delete()
        messages.info(request, 'Anime eliminado correctamente')
        return redirect('anime:listar')
    
    return render(request, 'delete.html', {'anime':anime})
from django.urls import path
from .views import home, agregar_anime, listar_animes, update_anime, delete_anime, detalle_anime

app_name = 'anime'

urlpatterns = [
    path('', home, name="home"),
    path('crear/', agregar_anime, name="crear"),
    path('listar/', listar_animes, name="listar"),
    path('update/<int:pk>/', update_anime, name="update"),
    path('delete/<int:pk>/', delete_anime, name="delete"),
    path('detalle/anime/<int:pk>/', detalle_anime, name="detalle"),
]
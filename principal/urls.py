from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('dinamico/', views.dinamico, name='dinamico'),
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('propietarios/', views.lista_propietarios, name='lista_propietarios'),
    path('mascotas/registrar/', views.registrar_mascota, name='registrar_mascota'),
    path('propietarios/registrar/', views.registrar_propietario, name='registrar_propietario'),
]

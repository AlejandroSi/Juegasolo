from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('mascota', views.mascotas, name='mascota'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('adopta', views.adopta, name='adopta'),
    path('contacto', views.contacto, name='contacto'),

]


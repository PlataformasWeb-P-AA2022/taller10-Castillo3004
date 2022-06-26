from django.urls import path 

from . import views

urlpatterns = [
    # ver
    path('', views.index, name= 'index'),
    path('barrio/<int:id>', views.obtener_barrio, name='obtener_barrio'),
    path('barrios', views.lista_barrios, name = 'lista_barrios'),
    # crear 
    path('crear/parroquia', views.crear_parroquia, name='crear_parroquia'),
    path('crear/barrio', views.crear_barrio, name='crear_barrio'),
    path('crear/barrio/parroquia/<int:id>', views.crear_barrio_parroquia, name='crear_barrio_parroquia'),
    # editar
    path('editar/parroquia/<int:id>',views.editar_parroquia, name='editar_parroquia'),
    path('editar/barrio/<int:id>',views.editar_barrio, name='editar_barrio'),
    # eliminar
    path('eliminar/parroquia/<int:id>', views.eliminar_parroquia, name='eliminar_parroquia'),
    path('eliminar/barrio/<int:id>', views.eliminar_barrio, name='eliminar_barrio'),
]

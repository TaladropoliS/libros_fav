from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('agregar', views.agregar, name='agregar'),
    path('add_favorito/<int:id>', views.add_favorito, name='add_favorito'),
    path('<int:id>', views.ver_libro, name='ver_libro'),
    path('del_favorito/<int:id>', views.del_favorito, name='del_favorito'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('eliminar_libro/<int:id>', views.eliminar_libro, name='eliminar_libro'),
    ]
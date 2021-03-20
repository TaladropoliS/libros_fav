from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_app.models import Usuario, Cuenta
from app_libros.models import Libros
from datetime import date
from django.contrib.auth import logout as do_logout
from django.db.models import Q, Max, Count, F
# Create your views here.

def books(request):
    if request.session['log_user']:
        context = {
            'libros': Libros.objects.all(),
            'libros_favoritos':  Usuario.objects.get(id=request.session['log_id']).libro_favorito.all()
        }
        return render(request, 'libros.html', context)
    return redirect('/')

def agregar(request):
    if request.session['log_user']:
        if request.method == "POST":
            if request.POST['titulo'] and request.POST['descripcion']:
                id = request.session['log_id']
                temp = Libros.objects.create(titulo=request.POST['titulo'],
                                             descripcion=request.POST['descripcion'],
                                             subido_por_id=Usuario.objects.get(id=id))
                return redirect('books')
            return redirect('books')
        return redirect('/')
    return redirect('/')

def add_favorito(request, id):
    if request.session['log_user']:
        user = Usuario.objects.get(id=request.session['log_id'])
        le_gusta = Libros.objects.get(id=id)
        print('TITULO ', le_gusta.titulo)
        le_gusta.le_gusta.add(user)
        return redirect('books')
    return redirect('/')

def ver_libro(request, id):
    if request.session['log_user']:
        context = {
            'user': Usuario.objects.get(id=request.session['log_id']),
            'libro': Libros.objects.get(id=id),
            'le_gusta': Libros.objects.get(id=id).le_gusta.all(),
            'libros': Libros.objects.all(),
        }
        return render(request, 'ver_libros.html', context)
    return redirect('/')

def del_favorito(request, id):
    if request.session['log_user']:
        user = Usuario.objects.get(id=request.session['log_id'])
        le_gusta = Libros.objects.get(id=id)
        le_gusta.le_gusta.remove(user)
        return redirect('books')
    return redirect('/')


def actualizar(request, id):
    if request.session['log_user']:
        if request.method == "POST":
            if request.POST['nuevo_titulo']:
                libro_act = Libros.objects.get(id=id)
                libro_act.titulo = request.POST['nuevo_titulo']
                libro_act.save()

            if request.POST['descripcion_libro']:
                desc_act = Libros.objects.get(id=id)
                desc_act.descripcion = request.POST['descripcion_libro']
                desc_act.save()

            return redirect('books')
        return redirect('/')
    return redirect('/')

def eliminar_libro(request, id):
    if request.method == "POST":
        libro_elim = Libros.objects.get(id=id)
        libro_elim.delete()
        return redirect('books')
    return redirect('/')
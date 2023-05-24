from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Curso

@login_required
def index(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/index.html', {'cursos_data':cursos})
    # return HttpResponse('cursos index')

@login_required
def crear(request):
    return render(request, 'cursos/crear.html')

@login_required
def guardar(request):
    curso = Curso()
    curso.codigo = request.POST['txt_codigo']
    curso.nombre = request.POST['txt_nombre']
    curso.creditos = int(request.POST['txt_creditos'])
    curso.save()
    return index(request)

@login_required
def detalle(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    return render(request, 'cursos/detalle.html', {'curso_data':curso})
    # return HttpResponse('detalle')

@login_required
def actualizar(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    curso.nombre = request.POST['txt_nombre']
    curso.creditos = int(request.POST['txt_creditos'])
    curso.save()
    return detalle(request, curso_id)

@login_required
def eliminar(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    curso.delete()
    return index(request)
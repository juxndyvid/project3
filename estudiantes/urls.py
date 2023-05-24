from django.urls import path

from . import views
from cursos import views as cursos
from core import views as core

app_name = 'estudiantes'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear, name='crear'),
    path('guardar/', views.guardar, name='guardar'),
    path('detalle/<int:estudiante_id>/', views.detalle, name='detalle'),
    path('actualizar/<int:estudiante_id>', views.actualizar, name='actualizar'),
    path('eliminar/<int:estudiante_id>', views.eliminar, name='eliminar'),
    path('cursos/', cursos.index, name='cursos'),
    path('salir/', core.cerrar, name='salir'),
]
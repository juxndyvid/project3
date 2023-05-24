from django.urls import path

from . import views
from estudiantes import views as estudiantes
from core import views as core

app_name = 'cursos'

urlpatterns = [
    path('', views.index, name='inicio'),
    path('crear/', views.crear, name='crear'),
    path('guardar/', views.guardar, name='guardar'),
    path('detalle/<int:curso_id>/', views.detalle, name='detalle'),
    path('actualizar/<int:curso_id>', views.actualizar, name='actualizar'),
    path('eliminar/<int:curso_id>', views.eliminar, name='eliminar'),
    path('estudiantes/', estudiantes.index, name='estudiantes'),
    path('salir/', core.cerrar, name='salir'),
]
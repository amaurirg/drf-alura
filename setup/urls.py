"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from clientes.views import ClientesViewSet
from escola.views import (
    AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno, ListaMatriculadosPorCurso, ImagemViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matriculas", MatriculasViewSet, basename="Matriculas")
router.register('clientes', ClientesViewSet, basename="Clientes")
router.register('imagens', ImagemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaMatriculadosPorCurso.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

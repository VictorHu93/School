from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet,CursoViewSet,MatriculaViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('estudantes', EstudanteViewSet, basename='Estudantes')
routers.register('cursos', CursoViewSet, basename='Cursos')
routers.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(routers.urls))
]

from django.contrib import admin
from django.urls import path
from .views import index, create, salvar, editar, update, deletar

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('salvar', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', deletar, name='delete')
]

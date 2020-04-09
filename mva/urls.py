from django.urls import path

from .views import CategoriaView, CategoriaNew, CategoriaEdit, \
    CategoriaDel

urlpatterns = [
    path('categorias/',CategoriaView.as_view(), name='list_categoria'),
    path('categorias/new',CategoriaNew.as_view(), name='new_categoria'),
    path('categorias/edit/<int:pk>',CategoriaEdit.as_view(), name='edit_categoria'),
    path('categorias/delete/<int:pk>',CategoriaDel.as_view(), name='del_categoria'),
]

from django.urls import path
from . import views
urlpatterns = [
    path('home/admin',views.home_admin,name = 'home/admin'),
    path('home/leitor',views.home_leitor,name = 'home/leitor'),
    path('home/admin/cadastrar_livros',views.cadastrar_livros,name = 'cadastrar_livros'),
    path('ver_livros/<int:id>',views.ver_livros,name = 'ver_livros'),
    path('ver_livros_leitor/<int:id>',views.ver_livros_leitor,name = 'ver_livros_leitor'),
    path('home/admin/validar_livros',views.validar_livros,name = 'validar_livros'),
    path('deletar_livro/<int:id>/', views.deletar_livro, name='deletar_livro'),
    path('home/admin/cadastrar_emprestimo',views.cadastrar_emprestimo,name = 'cadastrar_emprestimo'),
    





]

from django.urls import path
from . import views
urlpatterns = [
    path('home/admin',views.home_admin,name = 'home/admin'),
    path('home/leitor',views.home_leitor,name = 'home/leitor')

]

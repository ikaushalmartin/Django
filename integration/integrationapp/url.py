from django.urls import path
from . import views

urlpatterns = [
    path('hey',views.hey, name='hey'),
    path('fetchdata',views.fetchdata,name='fetchdata'),
    path('registeruser', views.registeruser,name='registeruser')

]
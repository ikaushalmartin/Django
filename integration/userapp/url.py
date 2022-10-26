from django.urls import path
from . import views


urlpatterns = [
    path('hey',views.hey, name='hey'),
    path('registeruser', views.registeruser,name='registeruser'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout')

]
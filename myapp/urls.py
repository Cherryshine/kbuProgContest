from django.urls import path, include
from requests import post 
from myapp import views
urlpatterns = [
    path('', views.loginpage),
    path('main', views.main, name='logincheck'),
    path('bokkeum/', views.Bokkeum),
    path('calmel/', views.Calmel),
    path('illip/', views.Illip),
    path('miral/', views.Miral),
    path('moria/', views.Moria),
]
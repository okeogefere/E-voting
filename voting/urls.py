from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('result/', views.result, name='result'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('vote/', views.vote, name='vote'),
]
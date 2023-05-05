from django.urls import path
from app_general import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
]

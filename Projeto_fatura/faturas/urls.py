from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Faturas-home'),
    path('sobre/', views.about, name='Faturas-about'),
    #path('login/', views.about, name='Faturas-about'),
    #path('signup/', views.about, name='Faturas-about'),
    #path('adicionar/', views.about, name='Faturas-about'),
]

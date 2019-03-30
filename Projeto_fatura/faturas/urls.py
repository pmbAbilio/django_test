from django.urls import path
from .views import FaturaListView, FaturaDetailView, FaturaCreateView, FaturaUpdateView, FaturaDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faturas/', FaturaListView.as_view(), name='Faturas-home'),
    path('fatura/<int:pk>/', FaturaDetailView.as_view(), name='Fatura'),
    path('fatura/nova/', FaturaCreateView.as_view(), name='Fatura-nova'),
    path('fatura/<int:pk>/editar/',
         FaturaUpdateView.as_view(), name='Fatura-editar'),
    path('fatura/<int:pk>/apagar/',
         FaturaDeleteView.as_view(), name='Fatura-apagar'),
    path('sobre/', views.about, name='Faturas-about'),
]

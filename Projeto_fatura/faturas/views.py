from django.shortcuts import render
from .models import Fatura


def home(request):
    return render(request, 'faturas/home.html', {'title': "Faturação", 'fatura': Fatura.objects.all()})


def about(request):
    return render(request, 'faturas/sobre.html')

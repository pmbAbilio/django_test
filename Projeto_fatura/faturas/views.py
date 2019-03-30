from django.shortcuts import render
from .models import Fatura
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    if request.user.is_authenticated:
        return render(request, 'faturas/home.html', {'title': "As minhhas faturas", 'fatura': Fatura.objects.filter(Client=request.user)})
    else:
        return render(request, 'faturas/homeUnauth.html')


class FaturaListView(ListView):
    template_name = 'faturas/home.html'
    context_object_name = 'fatura'
    ordering = ['-Data']

    def get_queryset(self):
        return Fatura.objects.filter(Client=self.request.user)


class FaturaDetailView(DetailView):
    model = Fatura


class FaturaCreateView(LoginRequiredMixin, CreateView):
    model = Fatura
    fields = ['Vendedor', 'Data', 'imagemUrl', 'Descricao', 'Valor']

    def form_valid(self, form):
        form.instance.Client = self.request.user
        return super().form_valid(form)


class FaturaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Fatura
    fields = ['Vendedor', 'Data', 'imagemUrl', 'Descricao', 'Valor']

    def form_valid(self, form):
        form.instance.Client = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Client:
            return True
        return False


class FaturaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Fatura
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Client:
            return True
        return False


def about(request):
    return render(request, 'faturas/sobre.html')

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cat, Breed

class CatListView(LoginRequiredMixin, ListView):
    model = Cat
    template_name = 'cats/cat_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breed_count"] = Breed.objects.count()
        return context
    


class CatCreateView(LoginRequiredMixin, CreateView):
    model = Cat
    success_url = reverse_lazy('cats:list_cat')
    fields = '__all__'


class CatUpdateView(LoginRequiredMixin, UpdateView):
    model = Cat
    success_url = reverse_lazy('cats:list_cat')
    fields = '__all__'


class CatDeleteView(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:list_cat')
    fields = '__all__'


class BreedListView(LoginRequiredMixin, ListView):
    model = Breed
    template_name = 'cats/breed_list.html'


class BreedCreateView(LoginRequiredMixin, CreateView):
    model = Breed
    success_url = reverse_lazy('cats:list_cat')
    fields = '__all__'


class BreedUpdateView(LoginRequiredMixin, UpdateView):
    model = Breed
    success_url = reverse_lazy('cats:list_cat')
    fields = '__all__'


class BreedDeleteView(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:list_cat')
    fields = '__all__'

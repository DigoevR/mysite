from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Auto, Make
from django.contrib.auth.mixins import LoginRequiredMixin


class ListAuto(LoginRequiredMixin, ListView):
    model = Auto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["make_count"] = Make.objects.all().count()
        return context


class CreateAuto(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto-list')


class UpdateAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto-list')


class DeleteAuto(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto-list')


class ListMake(LoginRequiredMixin, ListView):
    model = Make
    template_name = 'autos/makes_list.html'


class CreateMake(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:auto-list')


class UpdateMake(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:auto-list')


class DeleteMake(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:auto-list')

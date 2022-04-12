from django.shortcuts import render
from django.urls import reverse_lazy
from ads.owner import OwnerCreateView, OwnerDeleteView, OwnerDetailView, OwnerListView, OwnerUpdateView
from .models import Ad

class AdsListView(OwnerListView):
    model = Ad


class AdsDetailView(OwnerDetailView):
    model = Ad


class AdsCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']
    success_url = reverse_lazy('ads:ad_list')


class AdsUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    success_url = reverse_lazy('ads:ad_list')


class AdsDeleteView(OwnerDeleteView):
    model = Ad
    success_url = reverse_lazy('ads:ad_list')
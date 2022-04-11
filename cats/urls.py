from django.urls import path
from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatListView.as_view(), name='list_cat'),
    path('main/create', views.CatCreateView.as_view(), name='create_cat'),
    path('main/<int:pk>/update', views.CatUpdateView.as_view(), name='update_cat'),
    path('main/<int:pk>/delete', views.CatDeleteView.as_view(), name='delete_cat'),
    path('lookup', views.BreedListView.as_view(), name='list_breed'),
    path('lookup/create', views.BreedCreateView.as_view(), name='create_breed'),
    path('lookup/<int:pk>/update', views.BreedUpdateView.as_view(), name='update_breed'),
    path('lookup/<int:pk>/delete', views.BreedDeleteView.as_view(), name='delete_breed'),
]

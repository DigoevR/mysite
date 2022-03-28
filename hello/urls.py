from django.urls import path

from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.view_counter, name='view_counter'),
]

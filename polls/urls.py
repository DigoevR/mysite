from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
  path('', views.Index.as_view(), name='index'),
  path('<int:pk>/', views.Detail.as_view(), name='detail'),
  path('<int:pk>/results/', views.Results.as_view(), name='results'),
  path('<int:pk>/vote/', views.vote, name='vote'),
  path('owner', views.owner, name='own er')
]
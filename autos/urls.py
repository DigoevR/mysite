from django.urls import path
from . import views


app_name = 'autos'
urlpatterns = [
    path('', views.ListAuto.as_view(), name='auto-list'),
    path('main/create', views.CreateAuto.as_view(), name='auto-create'),
    path('main/<int:pk>/update', views.UpdateAuto.as_view(), name='auto-update'),
    path('main/<int:pk>/delete', views.DeleteAuto.as_view(), name='auto-delete'),
    path('lookup/', views.ListMake.as_view(), name='make-list'),
    path('lookup/create', views.CreateMake.as_view(), name='make-create'),
    path('lookup/<int:pk>/update', views.UpdateMake.as_view(), name='make-update'),
    path('lookup/<int:pk>/delete', views.DeleteMake.as_view(), name='make-delete'),
]

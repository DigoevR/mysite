from django.urls import path
from . import views

app_name = 'ads'
urlpatterns = [
    path('', views.AdsListView.as_view(), name='ad_list'),
    path('<int:pk>', views.AdsDetailView.as_view(), name='ad_detail'),
    path('create', views.AdsCreateView.as_view(), name='ad_create'),
    path('<int:pk>/update', views.AdsUpdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete', views.AdsDeleteView.as_view(), name='ad_delete'),
    path('<int:pk>/picture', views.stream_file, name='ad_picture'),
    path('<int:pk>/comment/create', views.CommentCreateView.as_view(), name='ad_comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='ad_comment_delete'),
    path('<int:pk>/favorite', views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]
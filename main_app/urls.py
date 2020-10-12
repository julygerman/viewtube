from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('videos/', views.videos_index, name='index'),
    path('videos/<int:video_id>', views.videos_detail, name='detail'),
    path('videos/create/', views.VideoCreate.as_view(), name='videos_create'),
    path('videos/<int:pk>/update', views.VideoUpdate.as_view(), name='videos_update'),
    path('videos/<int:pk>/delete', views.VideoDelete.as_view(), name='videos_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('videos/<int:video_id>/assoc_user/<int:user_id>/', views.assoc_user, name='assoc_user'),
    

]
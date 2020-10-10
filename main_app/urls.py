from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('user/', views.user_index, name='index'),
    # path('', views.video_index, name='videos_index'),

]
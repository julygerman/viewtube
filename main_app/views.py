from django.shortcuts import render
from .models import User, Video


# Create your views here.
def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})

def about(request):
  return render(request, 'about.html')

def user_index(request):
    return render(request, 'user/index.html')

# def video_index(request):
#     videos = request.user.tree_set.all()
#     return render(request, 'home.html', {'videos': videos})
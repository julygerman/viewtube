from django.shortcuts import render, redirect
from .models import User, Video
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})

def about(request):
  return render(request, 'about.html')

def videos_index(request):
    return render(request, 'videos/index.html')


def videos_detail(request, video_id):
      video = Video.objects.get(id=video_id)
      return render(request, 'videos/detail.html', {'video': video})



class VideoCreate(CreateView):
    model = Video
    fields = '__all__'
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class VideoUpdate(UpdateView):
    model = Video
    fields = ['description', 'name']

class VideoDelete(DeleteView):
    model = Video
    success_url = ''
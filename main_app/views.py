from django.shortcuts import render, redirect
from .models import get_user_model, Video
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.shortcuts import render


# Create your views here.
def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})

def about(request):
  return render(request, 'about.html')

def videos_index(request):
    videos = Video.objects.all()
    context= {'videos': videos}
    return render(request, 'videos/index.html', context)


def videos_detail(request, video_id):
      video = Video.objects.get(id=video_id)
      return render(request, 'videos/detail.html', {'video': video})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = SignupForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



def assoc_user(request, video_id, user_id):
  Video.objects.get(id=video_id).user.add(user_id)
  return redirect('detail', video_id=cat_id)




class VideoCreate(CreateView):
    model = Video
    fields = ['name', 'description', 'url']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class VideoUpdate(UpdateView):
    model = Video
    fields = ['description', 'name']

class VideoDelete(DeleteView):
    model = Video
    success_url = '/'
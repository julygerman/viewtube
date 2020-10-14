from django.shortcuts import render, redirect
from .models import get_user_model, Video
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, CommentForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
      comment_form = CommentForm()
      return render(request, 'videos/detail.html', {'video': video, 'comment_form': comment_form})

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


@login_required
def assoc_user(request, video_id, user_id):
  Video.objects.get(id=video_id).user.add(user_id)
  return redirect('detail', video_id=video_id)

@login_required
def add_comment(request, video_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        print('form is valid')
        new_comment = form.save(commit=False)
        new_comment.video_id = video_id
        new_comment.user_id = request.user.id
        new_comment.save()
    return redirect('detail', video_id=video_id)


class VideoCreate(CreateView, LoginRequiredMixin):
    model = Video
    fields = ['name', 'description', 'url']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class VideoUpdate(UpdateView, LoginRequiredMixin):
    model = Video
    fields = ['description', 'name']

class VideoDelete(DeleteView, LoginRequiredMixin):
    model = Video
    success_url = '/'
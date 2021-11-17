from django.shortcuts import render
from django.contrib import messages
from .forms import VideoForm
from .models import Video


def home(request):
    app_name = 'Coding Tutorials'
    return render(request, 'video_collection/home.html', {'app_name': app_name})


def add(request):

    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            new_video_form.save()
            messages.info(request, 'New video saved!')
            # todo show successful message or redirect to list of videos
        else:
            messages.info(request, 'Please check the data entered')
            return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_collection/video_list.html', {'videos': videos})
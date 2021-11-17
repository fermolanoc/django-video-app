from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .forms import VideoForm
from .models import Video


def home(request):
    app_name = 'Coding Tutorials'
    return render(request, 'video_collection/home.html', {'app_name': app_name})


def add(request):

    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            try:
                new_video_form.save()
                return redirect('video_list')
                # messages.info(request, 'New video saved!')
            # todo show successful message or redirect to list of videos
            except ValidationError:
                messages.warning(request, 'Invalid YouTube URL')
            except IntegrityError:
                messages.warning(request, 'You already added that video')
        
        messages.info(request, 'Please check the data entered')
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_collection/video_list.html', {'videos': videos})
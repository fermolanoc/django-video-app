from django.shortcuts import render


def home(request):
    app_name = 'Coding Tutorials'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

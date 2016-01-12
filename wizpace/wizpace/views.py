from django.shortcuts import render


def home(request):
    return render(request, 'wizpace/index.html', {})

def toc(request):
    return render(request, 'wizpace/toc.html', {})

def privacy(request):
    return render(request, 'wizpace/privacy.html', {})
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'comments/main.html')

def movie(request):
    return render(request, 'comments/movie.html')

def cartoon(request):
    return render(request, 'comments/cartoon.html')

def outlog(request):
    return render(request, 'registration/outlog.html')

def leon_full(request):
    return render(request, 'comments/leon_full.html')

def koko_full(request):
    return render(request, 'comments/koko_full.html')

def soul_full(request):
    return render(request, 'comments/soul_full.html')

def pirates_full(request):
    return render(request, 'comments/pirates_full.html')

def dolmatines_full(request):
    return render(request, 'comments/dolmatines_full.html')

def wishes_full(request):
    return render(request, 'comments/wishes_full.html')
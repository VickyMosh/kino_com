from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'comments/main.html')

def movie(request):
    return render(request, 'comments/movie.html')

def cartoon(request):
    return render(request, 'comments/cartoon.html')
from django.shortcuts import render
from django.db import models
from . import models
from django.views.generic import ListView
from .models import Price
from django.db.models import Q
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
    all_kino = models.Kino.objects.all()
    context = {'all_kino': all_kino}
    return render(request, 'comments/leon_full.html', context=context)

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

class SearchResultsView(ListView):
    model = Price
    template_name = 'comments/search_results.html'


class SearchResultsView(ListView):
    model = Price
    template_name = 'comments/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Price.objects.filter(
            Q(name__icontains=query) | Q(money__icontains=query)
        )
        return object_list
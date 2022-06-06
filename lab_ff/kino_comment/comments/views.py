from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.shortcuts import render
from django.views import generic
from django.db import models
from django.views.generic import ListView
from django.db.models import Q

from .models import Kino, Price, Comment


class MovieListView(generic.ListView):
    template_name = 'comments/list.html'

    def get_queryset(self):
        return Kino.objects.all()


class MovieDetailView(generic.DetailView):
    model = Kino
    template_name = 'comments/detail.html'

    def get_queryset(self):
        return Kino.objects.all()


def add_comment(request, film_id):
    film = get_object_or_404(Kino, pk=film_id)
    kwargs = request.POST
    if 'fname' in kwargs and 'message' in kwargs:
        new_comment = Comment(
            kino=film,
            author=kwargs['fname'],
            text=kwargs['message'],
        )
        new_comment.save()

    return HttpResponseRedirect(reverse('movie_list'))


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

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Price.objects.filter(
            Q(name__icontains=query) | Q(money__icontains=query)
        )
        return object_list

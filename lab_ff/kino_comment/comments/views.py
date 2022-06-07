from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.shortcuts import render
from django.views import generic
from django.db import models
from django.views.generic import ListView
from django.db.models import Q
from .models import Kino, Add, Price, Comment
from django.contrib import messages


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

def add(request):
   all_add = Add.objects.all()
   context = {'all_add': all_add}
   if request.POST:
       name = request.POST['name']
       kino = request.POST['kino']
       Add.objects.create(name=name, kino=kino)
       return render(request, 'comments/add.html', context=context)
   else:
       return render(request, 'comments/add.html', context=context)

def delete(request):
    all_add = Add.objects.all()
    context = {'all_add': all_add}
    if request.POST:
        name = request.POST['name']
        try:
            Add.objects.get(name=name).delete()
            return render(request, 'comments/delete.html', context=context)
        except:
            messages.info(request, 'Name not found!')
            return render(request, 'comments/delete.html', context=context)
    else:
        return render(request, 'comments/delete.html', context=context)


def edit(request):
    return render(request, 'comments/edit.html')

class SearchResultsView(ListView):
    model = Price
    template_name = 'comments/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Price.objects.filter(
            Q(name__icontains=query) | Q(money__icontains=query)
        )
        return object_list

# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from django.http import HttpResponse

from .models import Movie

# def index(request):
#     print(Movie.objects)
#     movie_list = Movie.objects.all()[:5]
#     output = ', '.join([m.title for m in movie_list])
#     return HttpResponse(output)
#     # return HttpResponse("Hello, world. You're at the polls index.")

class MovieListView(generic.ListView):
    """Show all movies."""
    model = Movie

class MovieDetailView(generic.DetailView):
    """Show the requested movie."""
    model = Movie

class MovieCreateView(generic.CreateView):
    """Create a new movie."""
    model = Movie
    fields = '__all__'

class MovieUpdateView(generic.UpdateView):
    """Update the requested movie."""
    model = Movie
    fields = '__all__'

class MovieDeleteView(generic.DeleteView):
    """Delete the requested movie."""
    model = Movie
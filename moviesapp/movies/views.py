# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.shortcuts import render
from django.db import IntegrityError


from django.http import HttpResponse

from .models import Movie, Review
from .forms import MovieForm

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Avg
from rest_framework import viewsets
from .serializers import MovieSerializer, ReviewSerializer



class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Movie
class MovieListView(generic.ListView):
    """Show all movies."""
    model = Movie
    # content = {
    #     'avg_review': Avg(movie.rating for movie in model.objects.all())
    # }
    # def get_context_data(self, **kwargs):
    #     # print(self)
    #     # print(kwargs)
    #     ctx = super(MovieListView, self).get_context_data(**kwargs)
    #     print('hi')
    #     ctx['rating'] = Review.objects.values('rating').annotate(average=Avg('rating'))
    #     print(ctx['rating'])
    #     return ctx

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        movies = self.get_queryset()
        data['review_dictionary'] = {}
        # for movie in movies:
            # print(movie.reviews)
            # data['review_dictionary'][movie.pk] = Avg(review.rating for review in movie.reviews)
        # print(data)
        return data

    def get_queryset(self):
        print('get queryset')
        movies = super().get_queryset()
        print(movies[0].reviews)
        return movies

class MovieDetailView(generic.DetailView):
    """Show the requested movie."""
    model = Movie

class MovieCreateView(SuccessMessageMixin, generic.CreateView):
    """Create a new movie."""
    model = Movie
    fields = '__all__'
    success_message = 'The movie created successfully'

class MovieUpdateView(generic.UpdateView):
    """Update the requested movie."""
    model = Movie
    fields = '__all__'

class MovieDeleteView(generic.DeleteView):
    """Delete the requested movie."""
    model = Movie

# Review
class ReviewCreate(generic.CreateView):
    model = Review
    fields = '__all__'
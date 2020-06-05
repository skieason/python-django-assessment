# -*- coding: utf-8 -*-
# from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', view=views.MovieListView.as_view(), name='index'),
    path('<int:pk>/', view=views.MovieDetailView.as_view(), name='detail'),
    path('create/', view=views.MovieCreateView.as_view(), name='create'),
    path('update/<int:pk>/', view=views.MovieUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', view=views.MovieDeleteView.as_view(success_url="/movies"), name='delete'),
]

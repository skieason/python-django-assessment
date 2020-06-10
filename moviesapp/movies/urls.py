# -*- coding: utf-8 -*-
# from django.conf.urls import url
from django.urls import path, include

from . import views

# router = routers.DefaultRouter()
# router.register('movie', views.MovieViewSet)
# router.register('review', views.ReviewViewSet)



urlpatterns = [
    # path('', views.index, name='index'),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', view=views.MovieListView.as_view(), name='index'),
    path('<int:pk>/', view=views.MovieDetailView.as_view(), name='detail'),
    path('create/', view=views.MovieCreateView.as_view(), name='create'),
    path('update/<int:pk>/', view=views.MovieUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', view=views.MovieDeleteView.as_view(success_url="/movies"), name='delete'),
    path('review/<int:movie_id>/', view=views.ReviewCreate.as_view(success_url="/movies"), name="review"),
]

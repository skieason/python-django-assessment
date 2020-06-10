# -*- coding: utf-8 -*-
from django.conf import settings
# from django.conf.urls import url
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView

from rest_framework import routers

from moviesapp.movies.urls import views

router = routers.DefaultRouter()
router.register('movies', views.MovieViewSet)
router.register('reviews', views.ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('m', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    path('movies/', include(('moviesapp.movies.urls', 'movies'), namespace='movies')),

    path(settings.ADMIN_URL, admin.site.urls),  # {% url 'admin:index' %}
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
app_name = 'moviesd'
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path('400/', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        path('403/', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        path('404/', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        path('500/', default_views.server_error),
    ]

# -*- coding: utf-8 -*-
from django.urls import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from .validators import validate_title
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), error_messages={'invalid':"Movie with this Title already exists."}, max_length=255, unique=True, blank=False, null=False, validators=[validate_title])
    year = models.PositiveIntegerField(default=2019)
    # Example: PG-13
    rated = models.CharField(max_length=64)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    # Todo: add Rating models

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'pk': self.pk})

class Review(models.Model):
    movie = models.ForeignKey(
        Movie, related_name="reviews", on_delete=models.CASCADE
    )
    review = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    comment = models.TextField()

    def __str__(self):
        return self.comment


    # def clean(self):
    #     # Don't allow draft entries to have a pub_date.
    #     print('hi', super().clean())
    #     # raise ValidationError(_('Movie with this Title already exists.'))
 

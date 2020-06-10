from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# from .models import Movie

def validate_title(value):
  """
  Let's validate the title for a movie
  """
  print('validate title', value)
  if value == 'Testing':
    print('Testing Title:')
    raise ValidationError('Movie with this Title already exists.')
  # print(Movie.objects.all())
  # if not value:
    # print('raising error!')
    # raise ValidationError('', 'invalid')
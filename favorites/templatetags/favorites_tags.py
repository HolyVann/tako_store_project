from django import template
from favorites.utils import get_user_favorites


register = template.Library()

@register.simple_tag()
def user_favorites(request):
  return get_user_favorites(request)

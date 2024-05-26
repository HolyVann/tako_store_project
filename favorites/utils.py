from favorites.models import Favorites


def get_user_favorites(request):
  if request.user.is_authenticated:
    return Favorites.objects.filter(user=request.user)

  if not request.session.session_key:
    request.session.create()
  return Favorites.objects.filter(session_key=request.session.session_key )

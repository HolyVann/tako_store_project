from django.http import JsonResponse
from django.shortcuts import redirect
from goods.models import Products
from .models import Favorites
from django.template.loader import render_to_string
from favorites.utils import get_user_favorites


def favorite_add(request):

  product_id = request.POST.get('product_id')

  product = Products.objects.get(id=product_id)

  exists = False

  if request.user.is_authenticated:
      favorites = Favorites.objects.filter(user=request.user, product=product)

      if not favorites.exists():
          Favorites.objects.create(user=request.user, product=product)

          exists = True

  else:
      favorites = Favorites.objects.filter(session_key=request.session.session_key, product=product)

      if not favorites.exists():
          Favorites.objects.create(session_key=request.session.session_key, product=product)

          exists = True

      if not favorites.exists():
          Favorites.objects.create(session_key=request.session.session_key, product=product)

          exists = True

  user_favorites = get_user_favorites(request)

  if exists:
    message = f'''<img class="favoritesMessage" src="{ product.image.url }"/>
    <div class="jq-container favoritesMessage">
      <div favoritesMessage>Добавлено в избранное</div> <div class="favoritesMessage">{product}</div>
    </div>'''
  else:
    message = f'''<img class="favoritesMessage" src="{ product.image.url }"/>
    <div class="jq-container favoritesMessage">
      <div favoritesMessage> В избранном</div> <div class="favoritesMessage">{product}</div>
    </div>'''
  if user_favorites.exists():
    favorites_items_html = render_to_string(
      "favorites/includes/favorites_product.html", {'favorites': user_favorites}, request=request
    )

  response_data = {
    'message': message,
    'favorites_items_html': favorites_items_html,
    'exists': exists,
  }

  return JsonResponse(response_data)



def favorite_remove(request):

  favorite_id = request.POST.get('favorite_id')

  favorite = Favorites.objects.get(id=favorite_id)
  quantity = favorite.quantity
  favorite.delete()

  user_favorites = get_user_favorites(request)

  if user_favorites.exists():
    favorites_items_html = render_to_string(
      "favorites/includes/favorites_product.html", {'favorites': user_favorites}, request=request
    )
  else:
    favorites_items_html = render_to_string(
      'favorites/includes/favorites_modal_empty.html'
    )

  response_data = {
    'favorites_items_html': favorites_items_html,
    'quantity_deleted': quantity,
  }

  return JsonResponse(response_data)

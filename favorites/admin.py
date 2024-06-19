from django.contrib import admin
from favorites.models import Favorites


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
  list_display = ['user_display', 'product_display']
  fields = ['user', 'product']


  def user_display(self, obj):
    if obj.user:
      return str(obj.user)
    return 'Анонимный пользователь'


  def product_display(self, obj):
    return str(obj.product.name)

  user_display.short_description = 'Имя пользователя'
  product_display.short_description = 'Товар'

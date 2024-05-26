from django.contrib import admin
from carts.models import Cart
from django.utils.safestring import mark_safe


class CartTabAdmin(admin.TabularInline):
  model = Cart
  fields = ['get_image', 'product_variant', 'quantity', 'created_timestamp']
  search_fields ='product_variant', 'quantity', 'created_timestamp'
  readonly_fields = ('created_timestamp', 'get_image', 'product_variant')
  extra = 1

  def get_image(self, obj):
    return mark_safe(f'<img src="{obj.product.image.url}" width="120" heigth="160">')

  get_image.short_description = 'Изображение'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
  list_display = ['user_display', 'product_display', 'quantity', 'created_timestamp',]
  list_filter = ['created_timestamp', 'user',]
  fields = ['user', 'product_variant', 'quantity']


  def user_display(self, obj):
    if obj.user:
      return str(obj.user)
    return 'Анонимный пользователь'


  def product_display(self, obj):
    return str(obj.product_variant)


  user_display.short_description = 'Имя пользователя'
  product_display.short_description = 'Товар'

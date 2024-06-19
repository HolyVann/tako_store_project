from django.contrib import admin
from goods.models import Categories, Products, Gallery, Brands, Sizes, Variants
from django.utils.safestring import mark_safe


class GalleryTabAdmin(admin.TabularInline):
  model = Gallery
  readonly_fields = ('get_image', )
  fields = [
    'get_image',
    'image',
  ]
  extra = 1

  def get_image(self, obj):
    return mark_safe(f'<img src="{obj.image.url}" width="120" heigth="160">')

  get_image.short_description = 'Изображение'


class VariantsTabAdmin(admin.TabularInline):
  model = Variants
  fields = [
    'product',
    'size',
    'quantity',
  ]
  extra = 1


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
  list_display = ['name',]


@admin.register(Brands)
class BrandssAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
  list_display = ['name',]


@admin.register(Sizes)
class SizesAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
  list_display = ['name',]


@admin.register(Variants)
class VariantsAdmin(admin.ModelAdmin):
  list_display = [
    'get_image',
    'product_display',
    'size',
    'quantity'
    ]

  def product_display(self, obj):
    name = f'{obj.product.brand} {obj.product.name}'
    return name

  def get_image(self, obj):
    return mark_safe(f'<img src="{obj.product.image.url}" width="120" heigth="160">')

  get_image.short_description = 'Изображение'

  product_display.short_description = 'Продукт'


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name', 'article')}
  list_display = ['get_image', 'name', 'category', 'price', 'discount', 'is_new']
  list_editable = ['discount',]
  search_fields = ['name', 'description']
  list_filter = ['discount', 'category']
  readonly_fields = ('get_image',)
  fields = [
    ('name', 'category'),
    'brand',
    'article',
    ('price', 'discount'),
    'is_new',
    ('get_image','image'),
    'slug',
    'description',
  ]

  inlines = [VariantsTabAdmin, GalleryTabAdmin]

  def get_image(self, obj):
    return mark_safe(f'<img src="{obj.image.url}" width="120" heigth="160">')

  get_image.short_description = 'Изображение'


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
  list_display = ['product_display',]
  fields = [
    'product',
    'image',
  ]

  def product_display(self, obj):
    return str(obj.product.name)

  product_display.short_description = 'Продукт'

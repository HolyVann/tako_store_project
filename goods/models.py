from django.db import models
from django.urls import reverse


class Categories(models.Model):
  name = models.CharField(max_length=150, unique=True, verbose_name='Название')
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

  class Meta:
    db_table = 'category'
    verbose_name = 'Категорию'
    verbose_name_plural = 'Категории'

  def __str__(self):
    return self.name


class Brands(models.Model):
  name = models.CharField(max_length=150, unique=True, null=True, blank=True, verbose_name='Название бренда')
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

  class Meta:
    db_table = 'brand'
    verbose_name = 'Бренд'
    verbose_name_plural = 'Бренды'

  def __str__(self):
    return self.name


class Products(models.Model):
  name = models.CharField(max_length=150, verbose_name='Название')
  slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
  description = models.TextField(blank=True, null=True, verbose_name='Описание')
  image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
  price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2,verbose_name='Цена')
  discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2,verbose_name='Скидка в %')
  category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
  article = models.CharField(max_length=50, unique=True, verbose_name='Артикул')
  brand = models.ForeignKey(to=Brands, on_delete=models.CASCADE, verbose_name='Бренд', blank=True, null=True)
  is_new = models.BooleanField(default=True, verbose_name='Новинка')

  class Meta:
    db_table = 'product'
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'
    ordering = ('id',)


  def __str__(self):
    return f'{self.brand} {self.name}'


  def get_absolute_url(self):
      return reverse("catalog:product", kwargs={"product_slug": self.slug})


  def sell_price(self):

    if self.discount:
      return round(self.price - self.price*self.discount/100, 2)

    return self.price


class Gallery(models.Model):
  product = models.ForeignKey(to=Products, on_delete=models.CASCADE, related_name='images')
  image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')

  class Meta:
    db_table = 'gallery'
    verbose_name = 'Изображение'
    verbose_name_plural = 'Галерея'

  def __str__(self):
    return self.product.name


class Sizes(models.Model):
  name = models.CharField(max_length=150, verbose_name='Размер')
  slug = models.SlugField(max_length=200, verbose_name='URL', blank=True, null=True)

  class Meta:
    db_table = 'size'
    verbose_name = 'Размер'
    verbose_name_plural = 'Размеры'

  def __str__(self):
    return self.name


class Variants(models.Model):
  product = models.ForeignKey(to=Products, on_delete=models.CASCADE, related_name='variants', verbose_name='Продукт')
  size = models.ForeignKey(to=Sizes, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Размер')
  quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

  def __str__(self):
    return f"{self.product.name} {self.size.name}"

  class Meta:
    db_table = 'variants'
    verbose_name = 'Вариант'
    verbose_name_plural = 'Варианты'

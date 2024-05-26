from django.shortcuts import render
from goods.models import Products, Gallery, Variants
from favorites.models import Favorites


def index(request):

  images = Gallery.objects.all()

  if request.user.is_authenticated:
    favorites = Favorites.objects.filter(user=request.user)

  title = 'TAKO STORE - МАГАЗИН МОДНОЙ МОЛОДЁЖНОЙ ОДЕЖДЫ'

  goods = Products.objects.order_by('-id')[:4]

  sale_goods = Products.objects.filter(discount__gt=0).order_by('id')[:4]

  new = Products.objects.filter(is_new=True)[:4]

  content = [
      {'title': 'Новинки',
      'url': 'goods:new'
      },
      {'title': 'Sale',
      'url': 'goods:sale'
      },
      {'title': 'Каталог',
      'url': 'goods:index'
      },
  ]

  slides = [
    {
    "image": "deps/media/takostore_by_1709730567_3317782932217921366_9909468511.jpg",
    },

    {
    "image": "deps/media/takostore_by_1710240690_3322062149600190219_9909468511.jpg",
    },

    {
    "image": "deps/media/takostore_by_1710145404_3321262833419777972_9909468511 (1).jpg",
    },

    {
    "image": "deps/media/takostore_by_1709730567_3317782932217921366_9909468511.jpg",
    },

    {
    "image": "deps/media/takostore_by_1710240690_3322062149600190219_9909468511.jpg",
    },

    {
    "image": "deps/media/takostore_by_1710145404_3321262833419777972_9909468511 (1).jpg",
    },

    {
    "image": "deps/media/takostore_by_1709730567_3317782932217921366_9909468511.jpg",
    },
    {
    "image": "deps/media/takostore_by_1709730567_3317782932217921366_9909468511.jpg",
    },

    {
    "image": "deps/media/takostore_by_1710240690_3322062149600190219_9909468511.jpg",
    },

    {
    "image": "deps/media/takostore_by_1710145404_3321262833419777972_9909468511 (1).jpg",
    },

    {
    "image": "deps/media/takostore_by_1709730567_3317782932217921366_9909468511.jpg",
    },

    {
    "image": "deps/media/takostore_by_1710240690_3322062149600190219_9909468511.jpg",
    },

    {
    "image": "deps/media/takostore_by_1710145404_3321262833419777972_9909468511 (1).jpg",
    },

    {
    "image": "deps/media/takostore_by_1709730567_3317782932217921366_9909468511.jpg",
    },

  ]

  instagram = 'https://www.instagram.com/takostore_by/?hl=ru'

  return render(request, "main/index.html", locals())


def about(request):

  title = "TAKO STORE - О нас"
  page_title = 'О нас'

  return render(request, 'main/about.html', locals())


def contacts(request):

  title = "TAKO STORE - Контакты"
  page_title = 'Контакты'

  return render(request, 'main/contacts.html', locals())

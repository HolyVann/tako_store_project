from django.shortcuts import render
from goods.models import Products, Categories, Gallery, Brands, Sizes, Variants
from django.core.paginator import Paginator
from goods.utils import q_search
from users.models import User
from carts.models import Cart
from favorites.models import Favorites



def catalog(request, category_slug="all"):

    order_by = request.GET.get('order_by', None)
    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)

    if query:
        goods = q_search(query)
    elif category_slug:
        if category_slug == 'all':
            goods = Products.objects.all().order_by('-is_new')
        elif category_slug:
            goods = Products.objects.filter(category__slug=category_slug)
    else:
        goods = Products.objects.all()


    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))

    context = {
        'title': "TAKO STORE - Каталог",
        'goods': current_page,
        'slug_url': category_slug,
        'page_title': 'Каталог',
    }

    return render(request, "goods/catalog.html", context)


def new(request, category_slug="all"):

    order_by = request.GET.get('order_by', None)

    if category_slug:
        if category_slug == 'all':
            goods = Products.objects.filter(is_new=True).order_by('-is_new')
        else:
            goods = Products.objects.filter(category__slug=category_slug).filter(is_new=True)
    else:
        goods = Products.objects.filter(is_new=True)


    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)


    page = request.GET.get('page', 1)
    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))

    context = {
        'title': 'TAKO STORE - Новинки',
        'page_title': 'Новинки',
        'slug_url': category_slug,
        'goods': current_page,
    }

    return render(request, "goods/new.html", context)


def sale(request, category_slug="all"):

    order_by = request.GET.get('order_by', None)

    if category_slug:
        if category_slug == 'all':
            goods = Products.objects.filter(discount__gt=0)
        else:
            goods = Products.objects.filter(category__slug=category_slug).filter(discount__gt=0)
    else:
        goods = Products.objects.filter(discount__gt=0)


    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)


    page = request.GET.get('page', 1)
    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))

    context = {
        'title': 'TAKO STORE - Sale',
        'page_title': 'Sale',
        'slug_url': category_slug,
        'goods': current_page,
    }

    return render(request, "goods/sale.html", context)


def product(request, product_slug, size_slug=None):

    product = Products.objects.get(slug=product_slug)

    goods = Products.objects.exclude(id=product.id).order_by('?')[:4]


    if size_slug:

        size = Sizes.objects.get(slug=size_slug)

        product_variant = Variants.objects.get(product=product, size=size)

        if request.user.is_authenticated:

            user_cart = Cart.objects.filter(user=request.user, product_variant=product_variant)

            if user_cart:
                product_in_cart = True

        else:

            user_cart = Cart.objects.filter(session_key=request.session.session_key, product_variant=product_variant)

            if user_cart:
                product_in_cart = True

        product_variants = product.variants.all()

        title = f"TAKO STORE - {product.name}, {product.article}"

        images = Gallery.objects.filter(product__slug=product_slug)

        return render(request, "goods/product_size.html", locals())


    product_variants = product.variants.all()

    # if request.user.is_authenticated:

    #     user_cart = Cart.objects.filter(user=request.user, product_variant=product_variant)

    #     if user_cart:
    #         product_in_cart = True

    # else:

    #     user_cart = Cart.objects.filter(session_key=request.session.session_key, product_variant=product_variant)

    #     if user_cart:
    #         product_in_cart = True

    title = f"TAKO STORE - {product.name}, {product.article}"

    images = Gallery.objects.filter(product__slug=product_slug)

    return render(request, "goods/product.html", locals())


def brands(request, brand_slug=None):

    if brand_slug:

        goods = Products.objects.filter(brand__slug=brand_slug)

        brand_name =  goods[0].brand.name

        title = f"TAKO STORE - {brand_name}"
        page_title = f'{brand_name}'

        return render(request, 'goods/brand_catalog.html', locals())
    else:

        brands = Brands.objects.all()

        title = f"TAKO STORE - Все бренды"
        page_title = 'Все бреды'

        return render(request, 'goods/all_brands.html', locals())

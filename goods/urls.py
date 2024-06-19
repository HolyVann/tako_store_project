from django.urls import path
from goods import views


app_name = 'goods'


urlpatterns = [
    path('', views.catalog, name='index'),

    path('search/', views.catalog, name='search'),

    path('brands/', views.brands, name='brands'),
    path('brands/<slug:brand_slug>/', views.brands_catalog, name='brand'),

    path('new/', views.new, name='new'),

    path('sale/', views.sale, name='sale'),

    path('product/<slug:product_slug>/', views.product, name='product'),
    path('product/<slug:product_slug>/<slug:size_slug>/', views.product, name='product'),

    path('<slug:category_slug>/', views.catalog_category, name='index'),
]

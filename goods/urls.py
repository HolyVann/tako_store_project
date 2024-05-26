from django.urls import path
from goods import views


app_name = 'goods'


urlpatterns = [
    path('', views.catalog, name='index'),
    path('brands/', views.brands, name='brands'),
    path('brands/<slug:brand_slug>/', views.brands, name='brand'),
    path('search/', views.catalog, name='search'),
    path('new/', views.new, name='new'),
    path('new/<slug:category_slug>/', views.new, name='new'),
    path('sale/', views.sale, name='sale'),
    path('sale/<slug:category_slug>/', views.sale, name='sale'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('product/<slug:product_slug>/<slug:size_slug>/', views.product, name='product'),
]

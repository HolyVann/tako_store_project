from django.urls import path
from favorites import views


app_name = 'favorites'


urlpatterns = [
    path('favorite-add/', views.favorite_add, name='favorite_add'),
    path('favorite-remove/', views.favorite_remove, name='favorite_remove'),
]

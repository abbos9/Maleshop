# imports 
from django.urls import path
from products.views import (WishListView, add_to_wishlist,ProductDetailView, add_to_card, PAGESHOPCARTVIEW)

app_name = 'products'

urlpatterns = [
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('<int:product_pk>/add_to_wishlist', add_to_wishlist, name= 'add_to_wishlist'),
    path('<int:pk>/shop_detail', ProductDetailView.as_view(),name= 'shop_details'),
    path('<int:pk>/add_to_card', add_to_card, name= 'add_to_card'),
    path('shop_cart/', PAGESHOPCARTVIEW.as_view(), name='shop_cart' ),
]


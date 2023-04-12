from django.urls import path
from .views import  shop_list, create_shop, update_shop,show_nearby_shop

app_name = "shop"

urlpatterns = [
  path("", shop_list, name="shop_list" ),
  path("create-shop/", create_shop, name="create_shop" ),
  path("update-shop/<int:pk>/", update_shop, name="update_shop" ),
  path("show-nearby-shop/", show_nearby_shop, name="show_nearby_shop"),
]
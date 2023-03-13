from django.urls import path
from .views import *
urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("cart/",cart,name="cart"),
    path("checkout/",checkout,name="checkout"),
    path("contact/",contact,name="contact"),
    path("login/",login,name="login"),
    path("my-account/",myAccount,name="my-account"),
    path("product-list/",productList,name="product-list"),
    path("product-detail/",productDetail,name="product-detail"),
    path("wishlist/",wishlist,name="wishlist"),
]
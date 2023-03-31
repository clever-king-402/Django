from .views import *
from django.urls import path, include
from rest_framework import routers
from . import views
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'categories', CategorySet)
router.register(r'sliders', SliderSet)
router.register(r'ads', AdSet)
router.register(r'brands',BrandSet)
router.register(r'products',ProductSet)
router.register(r'productreviews',ProductReviewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("categories/",views.getCategory,name='categories'),
    path("sliders/",views.getSlider,name='sliders'),
    path("ads/",views.getAd,name='ads'),
    path("brands/",views.getBrand,name='brands'),
    path("product-filter/<label>",views.getProductSale,name='products-sale'),
    path("products/<slug>",views.getProduct,name="product-details"),
    path("submit-review/<slug>",ReviewCRUD.as_view(),name="product-review"),
    path("createuser/",views.createUser,name="create-user")
]


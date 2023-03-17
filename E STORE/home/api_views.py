from .models import *
from .serializers import *
from rest_framework import  viewsets,filters

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

import django_filters.rest_framework
from rest_framework import generics

class ProductFilterView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category','labels']
    search_fields = ["name","description"]
    ordering_fields = ["id","price","name"]
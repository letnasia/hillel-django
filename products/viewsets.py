from rest_framework.authentication import BasicAuthentication
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from hillel_django.authentication import MyCustomAuthentication
from products.models import Product, Category, Store, StoreInventory
from rest_framework.permissions import IsAuthenticated
from products.serializers import (
    ProductSerializer,
    ProductViewSerializer,
    CategoryWithProductsSerializer,
    StoreSerializer,
    StoreProductsSerializer,
    StoreInventorySerializer,
    CategorySerializer,
    StoreInventorySerializerGet,
)


class ProductViewSet(ModelViewSet):
    # foreign key - select_related
    # many to many - prefetch_related
    queryset = Product.objects.all().select_related('category').prefetch_related('tags')
    authentication_classes = ()
    permission_classes = ()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductViewSerializer
        else:
            return ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    authentication_classes = ()
    permission_classes = ()

    def get_queryset(self):
        if self.request.method == 'GET':
            return self.queryset.prefetch_related('products')
        return self.queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryWithProductsSerializer
        return CategorySerializer


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all().prefetch_related('products')
    authentication_classes = ()
    permission_classes = ()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StoreProductsSerializer
        return StoreSerializer


class StoreInventoryViewSet(ModelViewSet):
    queryset = StoreInventory.objects.all().prefetch_related('product')
    authentication_classes = ()
    permission_classes = ()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StoreInventorySerializerGet
        return StoreInventorySerializer


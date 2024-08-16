from .views import *
from .views import *
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('product/all/', list_product, name='product_list'),
    path('product/all-filter/', product_list_with_filter, name='product_list_filter'),
    path('product/one-filter/', get_one_filter, name='product_one_filter'),
    path('product/more-filter/', get_more_filter, name='product_more_filter'),
    path('product/detail/<int:id>/', get_one_product, name='get_one_product'),

    path('supplier/', ListSupplier.as_view(), name='supplier_list'),
    path('supplier/create/', CreateSupplier.as_view(), name='supplier_create'),
    path('supplier/update/<int:pk>/', UpdateSupplier.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', DeleteSupplier.as_view(), name='supplier_delete'),
    path('supplier/detail/<int:pk>/', DetailSupplier.as_view(), name='supplier_detail'),

    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),

    path('api/', test_json, name='api_test'),
    path('api/orders/', order_api_list, name='api_order_list'),
    path('api/orders/<int:pk>/', order_api_detail, name='api_order_detail'),

    path('filter/', template_filter_django, name='template_filter_django'),
    path('tags/', template_tag_django, name='template_tag_django'),
]

router = routers.SimpleRouter()
router.register('api/products', ProductViewSet, basename='product')
router.register('api/product_simple', ProductViewSetDif, basename='product_simple')
router.register('api/supplier', SupplierViewSet, basename='supplier')
router.register('api/supply', SupplyViewSet, basename='supply')
router.register('api/parametr', ParametrViewSet, basename='parametr')
router.register('api/tag', TagViewSet, basename='tag')
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/warehouse', WarehouseViewSet, basename='warehouse')
router.register('api/inventory', InventoryViewSet, basename='inventory')
router.register('api/review', ReviewViewSet, basename='review')
router.register('api/supplier_simple', SupplierList, basename='supplier_simple')
router.register('api/product_pagination', ProductPaginationViewSet, basename='product_pagination')
urlpatterns += router.urls

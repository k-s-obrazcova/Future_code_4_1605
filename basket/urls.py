from django.urls import path
from .views import *

urlpatterns = [
    path('', basket_detail, name='basket_detail'),
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('remove/<int:product_id>/', basket_remove, name='basket_remove'),
    path('clear/', basket_clear, name='basket_clear'),
    path('buy/', basket_buy, name='basket_buy'),
]
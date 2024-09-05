from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from children_toys_shop.forms import OrderForm
from children_toys_shop.models import *

from rest_framework import viewsets
from children_toys_shop.serializer import *


def main(request):
    return render(request, 'index.html')


class ToysList(ListView):
    model = Toys
    template_name = 'toys/list.html'
    paginate_by = 10
    allow_empty = True

    def get_queryset(self):
        return Toys.objects.filter(is_exists=True)


class ToysDetail(DetailView):
    model = Toys
    template_name = 'toys/detail.html'


class MakerList(ListView):
    model = Maker
    template_name = 'maker/list.html'
    paginate_by = 6
    allow_empty = True


class MakerDetail(DetailView):
    model = Maker
    template_name = 'maker/detail.html'


class OrderList(ListView):
    model = Order
    template_name = 'order/list.html'
    allow_empty = True
    paginate_by = 12


class OrderCreate(CreateView):
    model = Order
    template_name = 'order/create.html'
    form_class = OrderForm


class OrderDetail(DetailView):
    model = Order
    template_name = 'order/detail.html'


#_______________________________API_____________________________________

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MakerViewSet(viewsets.ModelViewSet):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ToysViewSet(viewsets.ModelViewSet):
    queryset = Toys.objects.all()
    serializer_class = ToysSerializer


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = PosOrder.objects.all()
    serializer_class = PosOrderSerializer


class PosSupplyViewSet(viewsets.ModelViewSet):
    queryset = PosSupply.objects.all()
    serializer_class = PosSupplySerializer
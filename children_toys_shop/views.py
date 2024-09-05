from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from children_toys_shop.forms import OrderForm
from children_toys_shop.models import *

from rest_framework import viewsets
from children_toys_shop.serializer import *

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


def main(request):
    return render(request, 'index.html')


class ToysList(ListView):
    model = Toys
    template_name = 'toys/list.html'
    paginate_by = 10
    allow_empty = True

    def get_queryset(self):
        return Toys.objects.filter(is_exists=True)

@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('children_toys_shop.view_toys'), name='dispatch')
class ToysDetail(DetailView):
    model = Toys
    template_name = 'toys/detail.html'

@method_decorator(login_required(), name='dispatch')
class MakerList(ListView):
    model = Maker
    template_name = 'maker/list.html'
    paginate_by = 6
    allow_empty = True

@method_decorator(login_required(), name='dispatch')
class MakerDetail(DetailView):
    model = Maker
    template_name = 'maker/detail.html'

@method_decorator(login_required(), name='dispatch')
class OrderList(ListView):
    model = Order
    template_name = 'order/list.html'
    allow_empty = True
    paginate_by = 12

@method_decorator(login_required(), name='dispatch')
class OrderCreate(CreateView):
    model = Order
    template_name = 'order/create.html'
    form_class = OrderForm

@method_decorator(login_required(), name='dispatch')
class OrderDetail(DetailView):
    model = Order
    template_name = 'order/detail.html'


#_______________________________API_____________________________________
from rest_framework import permissions
class CustomPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]


class MakerViewSet(viewsets.ModelViewSet):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer
    permission_classes = [CustomPermission]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermission]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [CustomPermission]


class ToysViewSet(viewsets.ModelViewSet):
    queryset = Toys.objects.all()
    serializer_class = ToysSerializer
    permission_classes = [CustomPermission]


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer
    permission_classes = [CustomPermission]


class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = PosOrder.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermission]


class PosSupplyViewSet(viewsets.ModelViewSet):
    queryset = PosSupply.objects.all()
    serializer_class = PosSupplySerializer
    permission_classes = [CustomPermission]
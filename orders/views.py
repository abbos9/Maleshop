from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
# Models
from orders.models import OrderDetailModel, OrderModel, OrderItemModel
# forms 
from orders.forms import OrderDetailForm
from products.models import CupounModel, ProductModel
# Create your views here.

def Proceed_Order(request):
    cart = request.session.get('cart',[])
    if not cart:
        messages.add_message(request, messages.ERROR, "Order didn't create ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('orders:proceed_order')))
    products = ProductModel.get_from_cart(cart)
    order = OrderModel.objects.create(user=request.user, total_amount=0.0)
    total_amount = 0
    for product in products:
        total_amount += float(product.real_price())
        OrderItemModel.objects.create(order=order, product=product, quantity=1, price=product.price)
    if request.GET.get('total_amount'):
        total_amount = float(request.GET.get('total_amount'))
    code = request.GET.get("coupon")
    if code :
        updated_coupon = CupounModel.objects.get(code=code)
        updated_coupon.is_active = False
        updated_coupon.save()
    order.total_amount = float("{:.2f}".format(total_amount))
    order.save()
    request.session['cart'] = []
    messages.add_message(request, messages.SUCCESS, 'Order created successfully')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('orders:proceed_order')))

@login_required
def add_cart_data(request, pk , quantity):
    cart = request.session.get('cart_data', [])
    data = {
        'pk': pk,
        'quantity': quantity
    }
    if data in cart:
        cart.remove(data)
    else:
        cart.append(data)
    request.session['cart_data'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('orders:proceed_order')))


class CheckoutView(ListView):
    template_name = 'checkout.html'
    model =  ProductModel
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        in_cart = self.request.session.get('cart', [])
        products = ProductModel.get_from_cart(in_cart)
        context['products'] = products
        code = self.request.GET.get('coupon')
        order = self.request.session.get('order', {})
        try:
            coupon = CupounModel.objects.get(code=code)
            context['coupon'] = coupon
        except CupounModel.DoesNotExist:
            context['coupon'] = None
        return context

class Detail_Info(CreateView):
    model = OrderDetailModel
    form_class = OrderDetailForm
    template_name = 'checkout.html'
    success_url = reverse_lazy('orders:proceed_order')

class OrderHistoryView(ListView):
    template_name =  'history.html'
    model = OrderModel
    context_object_name = 'orders'
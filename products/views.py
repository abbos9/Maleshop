from typing import Any
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from products.models import(ProductModel,  WishListModel,CupounModel)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


class WishListView(ListView):
    template_name = 'wishlist.html'
    model = WishListModel
    context_object_name = 'wishlists'


@login_required()
def add_to_wishlist(request, product_pk):
    product = ProductModel.objects.get(pk=product_pk)
    try:
        WishListModel.objects.create(user=request.user, product=product)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse_lazy('pages:shop')))
    except IntegrityError:
        WishListModel.objects.get(user=request.user, product=product).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('pages:shop')))


class ProductDetailView(DetailView):
    template_name = 'shop-details.html'
    model = ProductModel
    context_object_name = 'shop_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = ProductModel.objects.filter(category=self.object.category).exclude(pk=self.object.pk)[:4]
        context['tags'] = ProductModel.objects.filter(tags__in=self.object.tags.all())
        context['categories'] = ProductModel.objects.filter(category=self.object.category)
        return context


@login_required()
def add_to_card(request, pk):
    cart =request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
        messages.success(request,'removed from card')
    else: 
        cart.append(pk)
        messages.success(request, 'added to card')
    request.session['cart'] = cart
    have_incart = request.GET.get('delete')
    if have_incart:
        cart.remove(pk)
    print(cart)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('pages:shop')))


class PAGESHOPCARTVIEW(ListView):
    template_name = 'shopping-cart.html'
    model = ProductModel
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        code = self.request.GET.get('coupon')
        try:
            coupon = CupounModel.objects.get(code=code)
            context['coupon'] = coupon
        except CupounModel.DoesNotExist:
            context['coupon'] = None
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        cart = self.request.session.get('cart', [])
        products = ProductModel.objects.filter(pk__in=cart)
        return products
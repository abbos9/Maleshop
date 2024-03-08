from typing import Any
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from products.models import( ProductModel,  WishListModel)
from django.contrib.auth.decorators import login_required

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
    else: 
        cart.append(pk)
    request.session['cart'] = cart
    have_incart = request.GET.get('delete')
    if have_incart:
        cart.remove(pk)
    print(cart)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('pages:shop')))


class PAGESHOPCARTVIEW(TemplateView):
    template_name = 'shopping-cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        products = ProductModel.objects.filter(pk__in=cart)
        context['products'] = products
        return context


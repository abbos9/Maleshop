from django import template
from datetime import datetime
from django.db.models import Sum, F, ExpressionWrapper, fields
# models
from products.models import ProductModel , WishListModel


register = template.Library()


@register.filter(name='in_wishlist')
def in_wishlist(user, product):
    return WishListModel.objects.filter(user=user, product=product).exists()


@register.filter(name='is_product_new')
def is_product_new(created_at):
    created_at_date = created_at.date()
    days_difference = (datetime.now().date() - created_at_date).days
    return days_difference <= 3  


@register.simple_tag(name='count')  
def count_of_products(request):
    cart = request.session.get('cart', [])
    count = len(cart)
    return count


# @register.simple_tag(name='total_price')
# def total_price(request):
#     cart = request.session.get('cart', [])
#     total = 0
#     for pk in cart:
#         product = ProductModel.objects.get(pk=pk)
#         total += product.real_price()
#     return total


@register.simple_tag(name='total_price')
def total_price(request):
    cart = request.session.get('cart', [])

    real_price_expression = ExpressionWrapper(
        F('price') - (F('discount') * (F('price') / 100)),
        output_field=fields.DecimalField(),
    )

    total = ProductModel.objects.filter(pk__in=cart).annotate(
        discounted_price=real_price_expression
    ).aggregate(total_price=Sum('discounted_price'))['total_price']

    return "{:.2f}".format(total) if total is not None else 0
from django import template
from django.db.models import Sum, F, ExpressionWrapper, fields
from django.contrib import messages
# models
from products.models import ProductModel , WishListModel


register = template.Library()


@register.filter(name='in_wishlist')
def in_wishlist(user, product):
    return WishListModel.objects.filter(user=user, product=product).exists()


@register.simple_tag(name='cart_info')
def get_cart_info(request, coupon=None):
    cart = request.session.get('cart', [])
    products = ProductModel.objects.filter(pk__in=cart)
    total_price = 0
    for product in products:
        total_price += product.real_price()
    quantity = len(cart)
    if coupon:
        total_price = total_price - (total_price * (coupon.discount_amount / 100))
    else:
        messages.success(request, "Coupon didn't be applied successfully!")
    return quantity, "{:.2f}".format(total_price)

@register.filter(name='in_cart')
def in_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        return True
    else:
        return False

# @register.simple_tag(name='total_price')
# def total_price(request):
#     cart = request.session.get('cart', [])
#     total = 0
#     for pk in cart:
#         product = ProductModel.objects.get(pk=pk)
#         total += product.real_price()
#     return total


# @register.simple_tag(name='total_price')
# def total_price(request):
#     cart = request.session.get('cart', [])

#     real_price_expression = ExpressionWrapper(
#         F('price') - (F('discount') * (F('price') / 100)),
#         output_field=fields.DecimalField(),
#     )

#     total = ProductModel.objects.filter(pk__in=cart).annotate(
#         discounted_price=real_price_expression
#     ).aggregate(total_price=Sum('discounted_price'))['total_price']

#     return "{:.2f}".format(total) if total is not None else 0
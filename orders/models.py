from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# models
from orders.choices import Status_Choices
from products.models import ProductModel
# Create your models here.

class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(_('total amount'), max_digits=10, decimal_places=2)
    status_choices = models.CharField(max_length=50, choices=Status_Choices.choices, default=Status_Choices.pending.value)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    
class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _('order item')
        verbose_name_plural = _('order items')

    def __str__(self):
        return f"Order Item #{self.order.id} - {self.product.name}"

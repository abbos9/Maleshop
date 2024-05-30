from django.contrib import admin
from orders.models import OrderModel, OrderItemModel, OrderDetailModel
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItemModel

admin.site.register(OrderDetailModel)


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount' , 'created_at',]
    inlines = [OrderItemInline]
from django.urls import path
from orders.views import OrderHistoryView, Proceed_Order, Detail_Info, CheckoutView
app_name = 'orders'

urlpatterns = [
    path('proceed_order/', Proceed_Order, name='proceed_order'),
    path("detail_info/", Detail_Info.as_view(), name='detail_info'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('history/', OrderHistoryView.as_view(), name='history'),
]
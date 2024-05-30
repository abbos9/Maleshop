from django import forms

# Models
from orders.models import OrderDetailModel
# Forms
class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetailModel
        fields = ['postcode', 'notes','Country','phone','town','address' ]
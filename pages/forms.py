from django.forms import ModelForm
from pages.models import ContactModel

class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'message']

from django.contrib import admin
from pages.models import CaruselModel, ContactModel
# Register your models here.
@admin.register(CaruselModel)
class CaruselModelAdmimn(admin.ModelAdmin):
    list_display = ['title', 'about', 'season', 'active']
    list_filter = ['active']
    list_editable = ['active']
    ordering = ['-created_at']
    search_fields = ['title','description',]
    

@admin.register(ContactModel)
class ContactModelAdmimn(admin.ModelAdmin):
    list_display = ['name', 'email', ]
    ordering = ['-created_at']
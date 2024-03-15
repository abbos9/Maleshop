from django.contrib import admin
from products.models import  (ColorModel, TagsModel, SizeModel, CategoryModel, BrandsModel, 
ProductModel, SubCategoryModel, WishListModel, ProductImagesModel, CupounModel)
# Register your models here.

# admin.site.register(CupinModel )

class ProductImagesModeInline(admin.TabularInline):
    model = ProductImagesModel

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name','description','quality','rating', 'category']
    search_fields = ('name','description','quality','rating', 'tags')
    list_filter = ['quality','rating']
    ordering = ['-pk']
    inlines = [ProductImagesModeInline]

@admin.register(WishListModel)
class WishListModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at','updated_at']
    ordering = ['-pk']

@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','updated_at','code']
    search_fields =['title','created_at','updated_at','code']
    list_filter = ['title','created_at','updated_at',]
    ordering = ['-pk']

@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','updated_at']
    search_fields =['title','created_at','updated_at']
    list_filter = ['title','created_at','updated_at',]
    ordering = ['-pk']

@admin.register(TagsModel)
class TagsModelAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','updated_at',]
    search_fields =['title','created_at','updated_at',]
    list_filter = ['title','created_at','updated_at',]
    ordering = ['-pk']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','updated_at',]
    search_fields =['title','created_at','updated_at',]
    list_filter = ['title','created_at','updated_at',]
    ordering = ['-pk']

@admin.register(BrandsModel)
class BrandsModelAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','updated_at',]
    search_fields =['title','created_at','updated_at',]
    list_filter = ['title','created_at','updated_at',]
    ordering = ['-pk']

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','updated_at',]
    search_fields =['title','created_at','updated_at',]
    list_filter = ['title','created_at','updated_at',]
    ordering = ['-pk']



from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# validator
from products.validator import rating_value_validator
# Create your models here


class CategoryModel(models.Model):
    title = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class BrandsModel(models.Model):
    title = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class SizeModel(models.Model):
    title = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class TagsModel(models.Model):
    title = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ColorModel(models.Model):
    title = models.CharField(max_length=20)
    code = models.CharField(max_length=8)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class SubCategoryModel(models.Model):
    title = models.CharField(max_length=30)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=5)
    image = models.ImageField(upload_to='Product')
    is_sale = models.BooleanField(default=False)
    quality = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=1, validators=[rating_value_validator])
    color = models.ManyToManyField(ColorModel) 
    tags = models.ManyToManyField(TagsModel)
    material = models.TextField(null=True, blank=True)
    sizes = models.ManyToManyField(SizeModel)
    brand = models.ForeignKey(BrandsModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ManyToManyField(SubCategoryModel)
    quantity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"={self.name}, price={self.price}, rating={self.rating}, colors={self.color.all()})"


    def is_new(self):
        current_time = timezone.now()
        diff = (current_time - self.created_at)
        if diff.days <= 3:
            return True
        else:
            return False

    def real_price(self):
        price = self.price
        discount = self.discount
        real_price = price - (discount * (price / 100))

        return round(real_price, 2)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class CupounModel(models.Model):
    code = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)
    discount_amount = models.DecimalField(max_digits=20, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupons'




class ProductImagesModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    image =  models.ImageField(upload_to='products/neasted_images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
    
    class Meta:
        verbose_name = 'product Image'
        verbose_name_plural = 'Product Images'


class WishListModel(models.Model):
    user  = models.ForeignKey(User, on_delete = models.CASCADE)
    product =  models.ForeignKey(ProductModel, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} | {self.created_at}"
    
    class Meta:
        verbose_name = 'WishList'
        verbose_name_plural = 'WishLists'
        unique_together = ['user', 'product']
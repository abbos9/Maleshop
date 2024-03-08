from django.db import models

# Create your models here.

class CaruselModel(models.Model):
    title = models.CharField(max_length=100)
    season  = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Hero/')
    active = models.BooleanField()
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title

    class Meta:
        verbose_name = "Carusel"
        verbose_name_plural = "Carusels"

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Blog')
    first_name = models.CharField(max_length=100)
    comments = models.IntegerField(default=0)
    phrase = models.TextField()
    phrase_creater_name = models.CharField(max_length=100)
    hashtag = models.CharField(max_length=100)

    def __str__(self) :
        return self.title

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

from django.db import models
from products.models import TagsModel
# Create your models here.

class AuthorModel(models.Model):
    full_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='post/avatar')
    date_of_birth = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.full_name
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'



class PostModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField()
    image = models.ImageField(upload_to='posts')
    tags = models.ManyToManyField(TagsModel)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_previous(self):
        return self.get_previous_by_created_at()
    
    def get_next(self):
        return self.get_next_by_created_at()
    
    def __str__(self) :
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'



class MessageModel(models.Model):
    message = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=50,)
    name = models.CharField(max_length=40,)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='message')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.message

    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
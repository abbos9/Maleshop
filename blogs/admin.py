from django.contrib import admin
from blogs.models import PostModel, AuthorModel, MessageModel
# Register your models here.

admin.site.register(PostModel)
admin.site.register(AuthorModel)
admin.site.register(MessageModel)
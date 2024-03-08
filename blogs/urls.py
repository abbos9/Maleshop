from django.urls import path
from blogs.views import blog_search_view

app_name = 'blogs'

urlpatterns = [
    path('blog/', blog_search_view, name='blog_search')
]
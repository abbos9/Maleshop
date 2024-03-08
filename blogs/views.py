from django.shortcuts import render
from django.views.generic import( DetailView, ListView)
from blogs.models import PostModel
# Create your views here.
def blog_search_view(request):
    q = request.GET.get('q')
    post = PostModel.objects.filter(tags_title__icontains=q)
    context = {'post': post}
    return render(request, 'blog.html', context=context)
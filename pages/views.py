# import
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView,ListView,DetailView, CreateView, FormView)
from blogs.models import PostModel
from pages.models import CaruselModel, ContactModel
from pages.forms import  ContactForm
# models
from products.models import (ProductModel, CategoryModel, TagsModel,ColorModel, SizeModel,BrandsModel)
from blogs.models import MessageModel, PostModel
# Create your views here.


class PAGEHOMEVIEW(ListView):
    model = CaruselModel.objects.filter(active=True)
    template_name = 'index.html'
    context_object_name = 'carusels'

    def get_queryset(self):
        return  CaruselModel.objects.filter(active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = PostModel.objects.all()[:3]
        context['products'] = ProductModel.objects.all()
        return context


class PAGEABOUTVIEW(TemplateView):
    template_name = 'about.html'

class PAGEBLOGDETAILVIEW(DetailView):
    template_name = 'blog-details.html'
    model = PostModel
    context_object_name = 'blog_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = MessageModel.objects.filter(post__id=self.object.id)
        return context



class PAGEBLOGVIEW(ListView):
    template_name = 'blog.html'
    model = PostModel
    context_object_name = 'blogs'

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        posts = PostModel.objects.all()
        if tag:
           posts = PostModel.objects.filter(tags__title=tag)
        return posts
    

def PageCommentView(request, pk):
    post = PostModel.objects.get(pk=pk)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        text = request.POST.get("message")
        MessageModel.objects.create(
            name=name, email=email,
            phone=phone, message=text,
            post=post
        )
    return redirect('pages:blog_detail', pk=pk)


class PAGECONTACTVIEW(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:contact')

class PAGESHOPVIEW(ListView):
    template_name = 'shop.html'
    model = ProductModel
    context_object_name = 'products'
    paginate_by = 2
    page_kwarg = 'page'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandsModel.objects.all()
        context['tags'] = TagsModel.objects.all()
        context['sizes'] = SizeModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        return context
    
    
    def get_queryset(self):
        product = ProductModel.objects.all().order_by('price')
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        size = self.request.GET.get('size')
        color = self.request.GET.get('color')
        tag = self.request.GET.get('tags')
        q = self.request.GET.get('q')
        min_price ,max_price = self.request.GET.get('min_price'), self.request.GET.get('max_price')
        sort = self.request.GET.get("sort")

        if sort:
           product = ProductModel.objects.all().order_by(sort)
        if category:
           product = ProductModel.objects.filter(category__title=category)
        if brand:
           product = ProductModel.objects.filter(brand__title=brand)
        if size:
           product = ProductModel.objects.filter(sizes__title=size)
        if color:
           product = ProductModel.objects.filter(color__title=color)
        if tag:
           product = ProductModel.objects.filter(tags__title=tag)
        if q:
            product = ProductModel.objects.filter(name__icontains=q)
        if min_price and max_price:
            product = ProductModel.objects.filter(price__range=(float(min_price), float(max_price)))
       
        return product
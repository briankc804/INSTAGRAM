from pyexpat import model
from django.shortcuts import render
from .forms import PostForm 
from .models import Post
from django.views.generic import (
    ListView,
    CreateView,
)
# Create your views here.

class PostListView(ListView):
    template_name = "insta/post_list.html"
    queryset= Post.objects.all()
    context_object_name = "posts"


class PostCreateView(CreateView):
    template_name = 'insta/post_create.html'
    model = Post
    fields =['image','caption']
    
    success_url = '/'
     
    
    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author =self.request.user
        return super().form_valid(form)  
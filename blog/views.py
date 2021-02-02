from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import Post

# Create your views here.


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'


class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body', 'image', 'image_url']

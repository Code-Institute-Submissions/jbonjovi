from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'

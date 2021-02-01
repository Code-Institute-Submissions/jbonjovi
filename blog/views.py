from django.views.generic import ListView
from blog.models import Post

# Create your views here.


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'

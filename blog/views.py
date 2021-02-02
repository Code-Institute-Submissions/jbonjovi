from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post

from django.urls import reverse_lazy


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


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')

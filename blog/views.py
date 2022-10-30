from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# def list(request):
#   Data = {'Post': Post.objects.all().order_by('-date')}
#   return render(request, 'blog/blog.html', Data)

class PostListView(ListView):
  queryset = Post.objects.all().order_by('-date')
  template_name = 'blog/blog.html'
  context_object_name = 'Post'
  paginate_by = 1

# def post(request, id):
#   post = Post.objects.get(id=id)
#   return render(request, 'blog/post.html', {'post': post})

class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/post.html'

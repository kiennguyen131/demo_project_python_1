from django.shortcuts import render
from .models import Post

def list(request):
  Data = {'Post': Post.objects.all().order_by('-date')}
  return render(request, 'blog/blog.html', Data)

def post(request, id):
  post = Post.objects.get(id=id)
  return render(request, 'blog/post.html', {'post': post})

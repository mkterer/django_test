from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def posts(request):
    return render(request, 'blog/posts.html', {})

def dddd(request):
    return render(request, 'blog/aaa.html', {})

def advans(request):
    return render(request, 'blog/advans.html', {})

def gets(request):
    print(Post.objects.all()) # >> post all
    print(User.objects.all()) # >> username all
    print(User.objects.get(username='test')) # >> test
    
    post = Post.objects.get(id='1')
    print(post.content) # >> 22222222
    post.content = 'test update'
    post.save() # update
    print(post.content) # >> test update
    
    delete_post = Post.objects.get(id='3')
    delete_post.delete() # >> records with id 3 are deleted
    return render(request, 'blog/gets.html', {})

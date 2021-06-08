from django.shortcuts import render

# Create your views here.
def posts(request):
    return render(request, 'blog/posts.html', {})

def dddd(request):
    return render(request, 'blog/aaa.html', {})

def advans(request):
    return render(request, 'blog/advans.html', {})

def gets(request):
    return render(request, 'blog/gets.html', {})

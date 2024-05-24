from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, 'posts/posts_list.html',context)

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'posts/post_page.html',context)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:list')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'posts/post_new.html',context)
from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
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
    
@login_required(login_url='/users/login/')
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:list')  # Redirect to the appropriate view after saving
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'posts/post_new.html',context)

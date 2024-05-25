from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form  = UserCreationForm()
    context = {'form': form} 
    return render(request, 'users/register.html',context)


def login_view(request):
    
    if request.method == 'POST':
        form =  AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user )
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:list')
    
    else :
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'users/login.html',context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:list')
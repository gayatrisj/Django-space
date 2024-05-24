from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','slug','banner']

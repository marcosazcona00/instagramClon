from django import forms
from post.models import Post
from django.forms import ModelForm

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'url_foto']
from .forms import *
from .models import Post
from user.models import User
from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from post.service.post_service import PostService 
from user.service.user_service import UserService 
from django.contrib.auth.decorators import login_required

# Create your views here.
class PostsListView(ListView):
    template_name = 'index.html'
    paginate_by = 10
    
    def __init__(self):
        self._user_service = UserService()
        
    def get_queryset(self):
        return self._user_service.get_posts_user(self.request.user.id)

class CreatePostView(View):
    def __init__(self):
        self._post_service = PostService()
    
    def get(self,request):
        return render(request,'new.html', {'form': CreatePostForm()})

    def post(self,request):
        form = CreatePostForm(request.POST)
        if form.is_valid():
            self._post_service.create(request.user.id, form.cleaned_data)
            return redirect(reverse('post:index_posts'))
        return render(request,'new.html', {'form': form})


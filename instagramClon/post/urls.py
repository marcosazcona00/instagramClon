from .views import *
from django.urls import path

app_name = 'posts'
urlpatterns = [
    path('', PostsListView.as_view(), name='index_posts'),
    path('new/', CreatePostView.as_view(), name = 'new_post'),
]

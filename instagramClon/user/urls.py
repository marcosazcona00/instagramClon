from .views import *
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('logout/', logout_user, name='logout'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('signup/', SignUpView.as_view(), name = 'signup'),
]

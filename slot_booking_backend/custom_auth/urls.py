from django.urls import path

from .views.login import login_user
from .views.register import register_user

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
]

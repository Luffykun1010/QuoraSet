from . import views
from django.contrib.auth import views as auth_views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.loginpage,name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('home',views.home,name='home'),
    path('comments',views.comments,name='comments'),
]
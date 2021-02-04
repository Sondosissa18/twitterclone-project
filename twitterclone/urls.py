"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LogoutView


from twitteruser import views as user_views


from authentication import views as auth_views

from tweet import views as tweet_views

from notification import views as notifica_views

urlpatterns = [
    path('', user_views.IndexView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('signup/', auth_views.Signup.as_view(), name='signup'),
    path('login/', auth_views.login_view, name='login'),
    path("addtweet/", tweet_views.AddTweetView.as_view(), name="add_tweet"),
    path("user/<int:user_id>/", tweet_views.UserDetailView.as_view(), name="user_detail"),
    path("following/<int:user_id>/", user_views.following_view, name="following"),
    path("tweet/<int:tweet_id>/", tweet_views.TweetDetailView.as_view(), name="tweet_detail"),
    path("notification/", notifica_views.notification_view, name="notification"),


    
]
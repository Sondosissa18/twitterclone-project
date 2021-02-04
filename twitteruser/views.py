from twitteruser.models import TwitterUser
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from notification.models import Notifications
# from .forms import AddFollowerForm
# from twitteruser.models import TwitterUser, TwitterFollowers
from twitteruser.models import TwitterUser
from itertools import chain
from django.views.generic import TemplateView, View


# def index_view(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("login"))
#     tweets = Tweet.objects.all().order_by('-created_at')
#     my_tweets = Tweet.objects.filter(user = request.user).order_by('-created_at')
#     followers = request.user.following.all()
#     following_tweet = []
#     for i, follow in enumerate(followers):
#         following_tweet += list(chain(Tweet.objects.filter(user =follow).order_by('-created_at')))

#     print(following_tweet)
#     notifications = Notifications.objects.filter(user = request.user, viewed = False).count()
#     context_dict = {"MyUser": settings.AUTH_USER_MODEL, "tweets": tweets, "followers":followers, "notifications": notifications, "my_tweets":my_tweets, "following_tweet":following_tweet}

#     return render(request, 'index.html', context_dict)


class IndexView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        tweets = Tweet.objects.all().order_by('-created_at')
        my_tweets = Tweet.objects.filter(user = request.user).order_by('-created_at')
        followers = request.user.following.all()
        following_tweet = []
        for i, follow in enumerate(followers):
            following_tweet += list(chain(Tweet.objects.filter(user =follow).order_by('-created_at')))

        print(following_tweet)
        notifications = Notifications.objects.filter(user = request.user, viewed = False).count()
        context_dict = {"MyUser": settings.AUTH_USER_MODEL, "tweets": tweets, "followers":followers, "notifications": notifications, "my_tweets":my_tweets, "following_tweet":following_tweet}

        return render(request, 'index.html', context_dict)

   

def following_view(request, user_id):
    if request.user.id == user_id:
        # you cant follow yourself
        return HttpResponseRedirect(reverse("home"))
    follows = TwitterUser.objects.get(id=user_id)
       
    allfollowers = request.user.following.all()
     
    if follows not in allfollowers:
        request.user.following.add(follows)
    else:
        request.user.following.remove(follows)
    return HttpResponseRedirect(reverse("home"))

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
# from authentication.forms import LoginForm, CustomUserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
# from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from .forms import AddTweetForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
import re
from django.contrib.auth.mixins import LoginRequiredMixin

from twitteruser.models import TwitterUser
from notification.models import Notifications


from django.views.generic import TemplateView, View


# def tweet_detail(request, tweet_id):
#     my_tweet = Tweet.objects.get(id=tweet_id)

#     return render(request, "tweet_detail.html", {"tweet": my_tweet})

class TweetDetailView(View):
    def get(self, request, tweet_id):
        my_tweet = Tweet.objects.get(id=tweet_id)

        return render(request, "tweet_detail.html", {"tweet": my_tweet})


# @login_required(login_url="/login")
# def add_tweet(request):

#     html = "generic_form.html"
#     if request.method == "POST":
#             form = AddTweetForm(request.POST)
#             if form.is_valid():
#                 data = form.cleaned_data
#                 current_tweet = Tweet.objects.create(
#                     user=request.user,
#                     text=data["text"],
#                 )
#                 current_tweet.save()
#                 users = re.findall("@(\\S*\\b)", data["text"])
#                 for current_user in users:
#                     notification = Notifications.objects.create(
#                         user=TwitterUser.objects.get(username=current_user[::]),
#                         tweet_id=Tweet.objects.get(id=current_tweet.id),
#                         viewed=False
#                     )
#                     notification.save()
#                 return HttpResponseRedirect(reverse("home"))
#     form = AddTweetForm()
#     return render(request, html, {"form": form})


class AddTweetView(LoginRequiredMixin, View):
    form_class = AddTweetForm
    def get(self, request):
        html = "generic_form.html"
        form = self.form_class()
        return render(request, html, {"form": form})

    def post(self, request):
        post_data = request.POST
        form = self.form_class(post_data)
        if form.is_valid():
            data = form.cleaned_data
            current_tweet = Tweet.objects.create(
                user=request.user,
                text=data["text"],
                )
            current_tweet.save()
            users = re.findall("@(\\S*\\b)", data["text"])
            for current_user in users:
                notification = Notifications.objects.create(
                    user=TwitterUser.objects.get(username=current_user[::]),
                    tweet_id=Tweet.objects.get(id=current_tweet.id),
                    viewed=False
                )
                notification.save()
            # return redirect(f"/tweet/{tweet.id}/")
            return HttpResponseRedirect(reverse("home"))


# def user_detail(request, user_id):
#     user = TwitterUser.objects.get(id=user_id)
#     tweets = Tweet.objects.all()
#     print(user)
#     return render(request, "user_detail.html", {"author": user, "tweets_list": tweets, "user": request.user})


class UserDetailView(View):
    def get(self, request, user_id):
        user = TwitterUser.objects.get(id=user_id)
        tweets = Tweet.objects.all()
        print(user)
        return render(request, "user_detail.html", {"author": user, "tweets_list": tweets, "user": request.user})



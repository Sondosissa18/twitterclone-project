from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from twitteruser.models import TwitterUser
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic.edit import CreateView
from tweet.models import Tweet
from notification.models import Notifications
from twitteruser.models import TwitterUser



@login_required(login_url="/login")
def notification_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.user.is_authenticated:
        notification_filter = Notifications.objects.filter(user=request.user, viewed=False)
        notifications = []
        for notification in notification_filter:
            tweet = Tweet.objects.get(id=notification.tweet_id.id)
            Notifications.objects.filter(user=request.user, viewed=False).delete()
            notifications.append(tweet)
        return render(request, "notification.html", {"notifications":notifications})
    return HttpResponseRedirect(reverse("login"))



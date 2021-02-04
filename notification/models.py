from twitteruser.models import TwitterUser
from django.db import models
from django.utils import timezone
from tweet.models import Tweet


class Notifications(models.Model):
    user = models.ForeignKey(TwitterUser, related_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    tweet_id = models.ForeignKey(Tweet, related_name="tweet_id", on_delete=models.CASCADE)  
    viewed = models.BooleanField(default=False)

    
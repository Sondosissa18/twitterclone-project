from django.db import models
from django.utils import timezone  
from twitteruser.models import TwitterUser

class Tweet(models.Model):
    user = models.ForeignKey(TwitterUser, related_name='tickets', on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=timezone.now)

 
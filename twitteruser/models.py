from django.db import models

from django.contrib.auth.models import AbstractUser

class TwitterUser(AbstractUser):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        # through="TwitterFollowers"
    )
    notifications = models.IntegerField(default=0)


    # follower = models.ForeignKey(TwitterUser, related_name='follower', on_delete=models.DO_NOTHING)
    # follows = models.ForeignKey(TwitterUser, related_name='follows', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.username

# class TwitterFollowers(models.Model):
#     follower = models.ForeignKey(TwitterUser, related_name='follower', on_delete=models.DO_NOTHING)
#     follows = models.ForeignKey(TwitterUser, related_name='follows', on_delete=models.DO_NOTHING)
    

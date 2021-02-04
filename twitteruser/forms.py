from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from twitteruser.models import TwitterUser, TwitterFollowers


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = TwitterUser
        fields = ('username', 'email')




from django import forms
# from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from tweet.models import Tweet

from twitteruser.models import TwitterUser
# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = Tweet
#         fields = ('username', 'email')


class AddTweetForm(forms.Form):
    # User = forms.CharField(max_length=100)
    # user = forms.ModelChoiceField(queryset=TwitterUser.objects.all())
    # user = forms.ModelChoiceField(queryset=TwitterUser.objects.all())

    # title = forms.CharField(max_length=10)
    text = forms.CharField(widget=forms.Textarea, max_length=140)
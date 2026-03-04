from django.forms import ModelForm
from django import forms
from .models import TeamMember, Portfolio, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class TeamMemberForm(ModelForm):
    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'role', 'bio', 'profile_image', 'linkedin_url', 'twitter_url', 'instagram_url']
        widgets = {
            'bio': forms.Textarea(),
        }

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'image', 'category']





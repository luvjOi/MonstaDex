from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from players.models import Player
from django import forms
from django.contrib.auth.models import User


class SignUp(UserCreationForm):
    player_name = forms.CharField(max_length=30, required=False, help_text='Please choose a player name')

    class Meta:
        model = User
        fields = ('username', 'player_name', 'password1', 'password2',)


def signup(request):
    form = SignUp(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        player_name = form.cleaned_data.get('player_name')
        user = authenticate(username=username, password=raw_password)
        Player.objects.create(name=player_name, user=user)
        login(request, user)
        return render(request, 'players/player_detail.html')
    return render(request, 'registration/signup.html', {'form': form})


class HomePageView(TemplateView):
    template_name = 'home_page.html'


def profile(request):
    form = AuthenticationForm(request.POST)
    return render(request, 'players/player_detail.html', {'form': form})

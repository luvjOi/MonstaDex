from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from players.models import Player
from django.urls import reverse_lazy


class SignUp(UserCreationForm):
    success_url = reverse_lazy('login')


def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            new_player = Player.objects.create(name=username)
            user.player = new_player
            user.player.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class HomePageView(TemplateView):
    template_name = 'home_page.html'

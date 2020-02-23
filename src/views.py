from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from players.models import Player
from rest_framework.response import Response

from src.api.serializers import PlayerSerializer


class HomePageView(TemplateView):
    template_name = 'home_page.html'


def new_player(request):
    add_player = Player.objects.create(name=request.user.player, user=request.user.username)
    add_player.user.player = add_player
    # add_player.user.player.save()
    add_player.save()
    serializer = PlayerSerializer(add_player, many=True, context={'request': request})
    return serializer.data


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        return super().post(self)



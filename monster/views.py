from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import MonstaSerializer
from monster.models import Monsta


class SiteMonsterView(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Monsta.objects.all()
    serializer_class = MonstaSerializer

    def list(self, request, *args, **kwargs):
        monsters = Monsta.objects.all()
        return render(request, 'monsters/monsters_list.html', context={'monsters': monsters})

    def retrieve(self, *args, **kwargs):
        monster = Monsta.objects.get(pk=kwargs['pk'])
        monster_count = Monsta.objects.all().count()
        first_id = Monsta.objects.first().id
        return render(self.request, 'monsters/monsters_detail.html',
                      context={'monster': monster, 'monster_count': monster_count, 'first_id': first_id})
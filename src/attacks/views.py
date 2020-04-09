from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import AttackSerializer
from attacks.models import Attack


class SiteAttackView(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Attack.objects.all()
    serializer_class = AttackSerializer

    def list(self, request, *args, **kwargs):
        attacks = Attack.objects.all()
        return render(request, 'attacks/attack_list.html', context={'attacks': attacks})

    def retrieve(self, *args, **kwargs):
        attack = Attack.objects.get(pk=kwargs['pk'])
        attack_count = Attack.objects.all().count()
        first_id = Attack.objects.first().id
        return render(self.request, 'attacks/attack_detail.html',
                      context={'attack': attack, 'attack_count': attack_count, 'first_id': first_id})



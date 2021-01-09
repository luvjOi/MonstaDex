import random

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from api.serializers import UserSerializer, GroupSerializer, MonstaSerializer, PlayerSerializer, AttackSerializer, \
    BindingSerializer
from attacks.models import Attack
from bindings.models import Binding
from monster.models import Monsta
from players.models import Player

ELEMENT = [
    'arcane',
    'light',
    'air',
    'water',
    'fire',
    'dark',
    'earth',
    'normal',
]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class APIMonstaViewSet(viewsets.ModelViewSet):
    queryset = Monsta.objects.all()
    serializer_class = MonstaSerializer


class APIPlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(detail=False, methods=['get'])
    def get_players_list(self, request):
        players_list = Player.objects.all()
        serializer = PlayerSerializer(players_list, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def get_player(self, request, pk):
        player = Player.objects.get(pk=pk)
        serializer = PlayerSerializer(player, many=False, context={"request": request})
        return Response(serializer.data)


class APIBindingViewSet(viewsets.ModelViewSet):
    queryset = Binding.objects.all()
    serializer_class = BindingSerializer

    @action(detail=False, methods=['get'])
    def get_monsters(self, request):
        monsters = Binding.objects.all().filter(player=self.request.user.player)
        serializer = BindingSerializer(monsters, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def pick_monster(self, request, pk):
        monster = Binding.objects.get(pk=pk)
        if monster.player.full_party and not monster.picked:
            raise ValidationError("You already have 3 picked monsters!")
        monster.picked = not monster.picked
        monster.save()
        monster.player.save()
        serializer = BindingSerializer(monster, many=False, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def pick_attacks(self, request, pk):
        monster = Binding.objects.get(pk=pk)
        monster.attacks.clear()
        for attack in request.data:
            attack = Attack.objects.get(pk=attack)
            monster.attacks.add(attack)
        if monster.attacks.count() > 4:
            raise ValidationError("You're only allowed to choose up to four awesome attacks")
        monster.save()
        serializer = BindingSerializer(monster, many=False, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def delete_binding(self, pk):
        remove_mon = Binding.objects.get(pk=pk)
        remove_mon.delete()
        print("This is a test")
        return Response(None)

    @action(detail=False, methods=['post'])
    def create_binding(self, request):
        monster = Monsta.objects.get(monsterName=request.data['monster']['monsterName'])
        mon = request.data['monster']
        add_mon = Binding.objects.create(player=request.user.player, monster=monster)
        while add_mon.attacks.count() < 4:
            attack_list = Attack.objects.all()
            random_atk = random.choice(attack_list)
            add_mon.attacks.add(random_atk)
        serializer = BindingSerializer(add_mon, many=False, context={'request': request})
        return Response(serializer.data)


class APIAttackViewSet(viewsets.ModelViewSet):
    queryset = Attack.objects.all().order_by('-name')
    serializer_class = AttackSerializer

    @action(detail=False, methods=["get"])
    def get_attacks(self, request):
        attacks = Attack.objects.all().order_by('pk')
        serializer = AttackSerializer(attacks, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['PUT'])
    def get_attacks_by_type(self, request):
        data = request.data.lower()
        attacks = Attack.objects.all()
        if data == "":
            serializer = AttackSerializer(attacks, many=True, context={'request': request})
        else:
            returned_attacks = []
            for attack in attacks:
                if request.data.lower() in attack.element.lower():
                    returned_attacks.append(attack)
            if len(returned_attacks) == 0:
                return Response([])
            serializer = AttackSerializer(returned_attacks, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['PUT'])
    def get_attacks_by_name(self, request):
        data = request.data.lower()
        attacks = Attack.objects.all()
        if data == "":
            serializer = AttackSerializer(attacks, many=True, context={'request': request})
        else:
            returned_attacks = []
            for attack in attacks:
                if request.data.lower() in attack.name.lower():
                    returned_attacks.append(attack)
            serializer = AttackSerializer(returned_attacks, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['PUT'])
    def get_attacks_my_monsters_have(self, request):
        player = request.user.player
        monsters = player.binding.all()
        my_attacks = []
        for mon in monsters:
            for attack in mon.attacks.all():
                my_attacks.append(attack)
        if request.data != "":
            searched_attacks = []
            for attack in my_attacks:
                if request.data.lower() in attack.name.lower():
                    searched_attacks.append(attack)
            serializer = AttackSerializer(searched_attacks, many=True, context={'request': request})
        else:
            serializer = AttackSerializer(my_attacks, many=True, context={'request': request})
        return Response(serializer.data)


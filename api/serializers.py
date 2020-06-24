from django.contrib.auth.models import User, Group
from rest_framework import serializers
from attacks.models import Attack
from bindings.models import Binding
from monster.models import Monsta
from players.models import Player


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'groups'
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url',
            'name'
        ]


class MonstaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monsta
        fields = [
            'id',
            'monsterName',
            'family',
            'element',
            'description',
            'image',
            'element_logo',
        ]


class AttackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attack
        fields = (
            'id',
            'name',
            'element',
            'image',
            'description',
        )


class BindingSerializer(serializers.ModelSerializer):
    assigned = serializers.ReadOnlyField(source='player.assigned')
    full_party = serializers.ReadOnlyField(source='player.full_party')
    attacks = AttackSerializer(required=False, many=True)
    monsterName = serializers.ReadOnlyField(source='monster.monsterName')
    description = serializers.ReadOnlyField(source='monster.description')
    element = serializers.ReadOnlyField(source='monster.element')
    image = serializers.ReadOnlyField(source='monster.image')
    picked = serializers.ReadOnlyField()
    element_logo = serializers.ReadOnlyField(source='monster.element_logo')
    family = serializers.ReadOnlyField(source='monster.family')

    class Meta:
        model = Binding
        fields = (
            'id',
            'assigned',
            'full_party',
            'level',
            'damageDealt',
            'picked',
            'image',
            'attacks',
            'monsterName',
            'description',
            'element',
            'killed',
            'element_logo',
            'family'
        )


class PlayerSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    binding = BindingSerializer(many=True)

    class Meta:
        model = Player
        fields = (
            'id',
            'name',
            'user',
            'lifespan',
            'binding',
            'full_party',
            'url',
        )

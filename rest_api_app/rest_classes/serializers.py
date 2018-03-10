# -*- coding: utf-8 -*-

from rest_framework import serializers

from pizza_auth_app.models import CustomUser
from pizza_app.models import PizzaMenuItem, PizzaIngredient


class PizzaMenuItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class is used to get the pizza menu items.
    But it does not show ingredients.

    TODO: add ingredients
    """
    ingredients = serializers.PrimaryKeyRelatedField(many=True,
                                                     queryset=PizzaIngredient.objects.all())
    class Meta:
        model = PizzaMenuItem
        fields = ('id', 'name', 'ingredients')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class is used to show users, but favourite_pizza can not be saved.


    """
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'our_note',
            'favourite_pizza',
        )

    favourite_pizza = serializers.SlugRelatedField(
        slug_field='name', queryset=PizzaMenuItem.objects.all())

    # def update(self, instance, validated_data):
    #     favourite_pizza = validated_data.pop('favourite_pizza')
    #     favourite = PizzaMenuItem.objects.get(name=favourite_pizza['name'])
    #     validated_data['favourite_pizza'] = favourite.id
    #     obj = CustomUser.objects.get(pk=instance.id)
    #     obj.favourite_pizza = favourite
    #     obj.username = validated_data['username']
    #     obj.email = validated_data['email']
    #     obj.our_note = validated_data['our_note']
    #     obj.save()
    #
    #     return obj
    #
    # def create(self, validated_data):
    #     favourite_pizza = validated_data.pop('favourite_pizza')
    #     favourite = PizzaMenuItem.objects.get(name=favourite_pizza['name'])
    #     validated_data['favourite_pizza'] = favourite
    #     obj = CustomUser(**validated_data)
    #
    #     obj.save()
    #
    #     return obj

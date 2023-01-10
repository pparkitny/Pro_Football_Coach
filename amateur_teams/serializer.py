from rest_framework import serializers
from .models import Coach, Team, Player, Stats, Pace, Shoting, Passing, Dribling, Defending, Physicality, Goalkeeping


class CoachSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    surname = serializers.CharField(required=True, max_length=100)
    team = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['name']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Coach.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.team = validated_data.get('team', instance.team)
        instance.save()
        return instance

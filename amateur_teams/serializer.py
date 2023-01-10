from rest_framework import serializers
from .models import Coach, Team, Player, Stats, Pace, Shoting, Passing, Dribling, Defending, Physicality, Goalkeeping


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ['id', 'name', 'surname', 'team']

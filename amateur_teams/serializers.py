from rest_framework import serializers
from .models import Coach, Team, Player, Stats, Pace, Shoting, Passing, Dribling, Defending, Physicality, Goalkeeping


class CoachSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name')

    class Meta:
        model = Coach
        fields = ['id', 'name', 'surname', 'team_name']

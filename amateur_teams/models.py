from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Coach(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)


class Team(models.Model):
    name = models.CharField(max_length=128)


class Player(models.Model):
    POSITION_CHOICES = [
        ('goalkeeper', 'Goalkeeper'),
        ('right_back', 'Right-back'),
        ('right_wing_back', 'Right Wing Back'),
        ('left_back', 'Left-back'),
        ('left_wing_back', 'Left Wing Back'),
        ('centre_back', 'Centre-back'),
        ('central_defensive_midfielder', 'Central Defensive Midfielder'),
        ('central_midfielder', 'Central Midfielder'),
        ('central_attacking_midfielder', 'Central Attacking Midfielder'),
        ('left_midfielder', 'Left Midfielder'),
        ('right_midfielder', 'Right Midfielder'),
        ('left_winger', 'Left Minger'),
        ('right_winger', 'Right Minger'),
        ('centre_forward', 'Centre Forward'),
        ('striker', 'Striker'),
    ]

    RIGHT_FOOT = 'right_foot'
    LEFT_FOOT = 'left_foot'

    FOOT_CHOICES = [
        (RIGHT_FOOT, 'Right'),
        (LEFT_FOOT, 'Left'),
    ]

    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    position = models.CharField(max_length=128, choices=POSITION_CHOICES)
    preferred_foot = models.CharField(
        max_length=128, choices=FOOT_CHOICES, default=RIGHT_FOOT)
    stats = models.OneToOneField('Stats', on_delete=models.CASCADE)


class Stats(models.Model):
    pace = models.OneToOneField('pace', on_delete=models.CASCADE)
    shoting = models.OneToOneField('shoting', on_delete=models.CASCADE)
    passing = models.OneToOneField('passing', on_delete=models.CASCADE)
    dribling = models.OneToOneField('dribling', on_delete=models.CASCADE)
    defending = models.OneToOneField('defending', on_delete=models.CASCADE)
    physicality = models.OneToOneField('physicality', on_delete=models.CASCADE)
    goalkeeping = models.OneToOneField('physicality', on_delete=models.CASCADE)

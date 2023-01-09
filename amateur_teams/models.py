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
    pace = models.OneToOneField('Pace', on_delete=models.CASCADE)
    shoting = models.OneToOneField('Shoting', on_delete=models.CASCADE)
    passing = models.OneToOneField('Passing', on_delete=models.CASCADE)
    dribling = models.OneToOneField('Dribling', on_delete=models.CASCADE)
    defending = models.OneToOneField('Defending', on_delete=models.CASCADE)
    physicality = models.OneToOneField('Physicality', on_delete=models.CASCADE)
    goalkeeping = models.OneToOneField('Goalkeeping', on_delete=models.CASCADE)


class Pace(models.Model):
    sprint_speed = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    acceleration = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])


class Shoting(models.Model):
    finishing = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    positioning = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    shot_power = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    long_shots = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    penalties = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    volleys = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])


class Passing(models.Model):
    vision = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    crossing = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    fk_accuracy = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    long_passing = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    short_passing = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    curve = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])


class Dribling(models.Model):
    agility = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    balance = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    reactions = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    composure = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    ball_control = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    dribbling = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])


class Defending(models.Model):
    interceptions = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    heading_accuracy = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    defensive_awareness = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    standing_tackle = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    sliding_tackle = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])


class Physicality(models.Model):
    jumping = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    stamina = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    strength = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    aggression = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])


class Goalkeeping(models.Model):
    gk_diving = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    gk_handling = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    gk_kicking = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    gk_positioning = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    gk_reflexes = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])

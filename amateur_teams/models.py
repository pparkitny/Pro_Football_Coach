from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Coach(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname} - Coach of {self.team}"


class Team(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


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

    def __str__(self):
        return f"{self.name} {self.surname} - Player from {self.team}"


class Stats(models.Model):
    pace = models.OneToOneField('Pace', on_delete=models.CASCADE)
    shoting = models.OneToOneField('Shoting', on_delete=models.CASCADE)
    passing = models.OneToOneField('Passing', on_delete=models.CASCADE)
    dribling = models.OneToOneField('Dribling', on_delete=models.CASCADE)
    defending = models.OneToOneField('Defending', on_delete=models.CASCADE)
    physicality = models.OneToOneField('Physicality', on_delete=models.CASCADE)
    goalkeeping = models.OneToOneField('Goalkeeping', on_delete=models.CASCADE)


class Pace(models.Model):
    # The speed with which a player walks or runs.
    sprint_speed = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # Defines the speed rate of a player’s sprinting.
    acceleration = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The rate at which a player’s running speed increases.


class Shoting(models.Model):
    # A player’s general shooting strength and accuracy.
    finishing = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The ability of a player to score.
    positioning = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # Defines a player’s ability to spot open space and move into good positions that offer an attacking advantage
    shot_power = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The strength of a player’s shoots.
    long_shots = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s accuracy for the shots taking from long distances.
    penalties = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s accuracy for taking penalty shots.
    volleys = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The ability of a player to perform volleys.


class Passing(models.Model):
    # Determines how accurate a player passes the ball to a teammate
    vision = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s mental awareness about his teammates’ positioning, for passing the ball to them.
    crossing = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The quality and accuracy of a player’s crosses.
    fk_accuracy = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The precision with which a player takes free kicks.
    long_passing = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s accuracy for the long passes.
    short_passing = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s accuracy for the short passes.
    curve = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s ability to curve the ball when passing and shooting.


class Dribling(models.Model):
    # A player’s ability to carry the ball and past an opponent.
    agility = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # Determines a player’s ability to manage and control the ball quickly and gracefully.
    balance = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The even distribution of enabling a player to remain upright and keep going.
    reactions = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s reaction time in response to events taking place around them.
    composure = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s the state or feeling of being calm and in control of their frustration.
    ball_control = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s ability to keep possession of the ball.
    dribbling = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s ability to carry the ball and past an opponent.


class Defending(models.Model):
    # A player’s ability to defend.
    interceptions = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The ability of a player to intercept the ball.
    heading_accuracy = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s accuracy when using the head to pass, shoot or clear the ball.
    defensive_awareness = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s ability to defend.
    standing_tackle = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The ability of performing standing tackle.
    sliding_tackle = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The ability to pull off a sliding tackle.


class Physicality(models.Model):
    # Represent the physical and bodily state of a player.
    jumping = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The ability of a player to jump off the ground for headers.
    stamina = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # player’s ability to sustain prolonged physical or mental effort
    strength = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # The quality or state of being physically strong.
    aggression = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A player’s degree of aggressiveness.


class Goalkeeping(models.Model):
    # A player’s ability to be a goalkeeper
    gk_diving = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # Ability to 'dive' for a ball
    gk_handling = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # Ability to catch the ball
    gk_kicking = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # Ability to make long and accurate kicks of the ball
    gk_positioning = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # Ability to position as goalkeeper
    gk_reflexes = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])  # A goalkeeper reaction time in response to events taking place around him.

# Generated by Django 4.1.5 on 2023-01-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amateur_teams', '0002_player_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('goalkeeper', 'Goalkeeper'), ('right_back', 'Right-back'), ('right_wing_back', 'Right Wing Back'), ('left_back', 'Left-back'), ('left_wing_back', 'Left Wing Back'), ('centre_back', 'Centre-back'), ('central_defensive_midfielder', 'Central Defensive Midfielder'), ('central_midfielder', 'Central Midfielder'), ('central_attacking_midfielder', 'Central Attacking Midfielder'), ('left_midfielder', 'Left Midfielder'), ('right_midfielder', 'Right Midfielder'), ('left_winger', 'Left Winger'), ('right_winger', 'Right Winger'), ('centre_forward', 'Centre Forward'), ('striker', 'Striker')], max_length=128),
        ),
    ]

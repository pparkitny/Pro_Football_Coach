# Generated by Django 4.1.5 on 2023-01-10 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amateur_teams', '0004_alter_coach_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='team',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='amateur_teams.team'),
        ),
    ]

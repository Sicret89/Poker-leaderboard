# Generated by Django 3.2.9 on 2022-12-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_player_jocker_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='logo_image',
            field=models.ImageField(default='logo_akvs47-main.png', upload_to='logo_pics'),
        ),
    ]

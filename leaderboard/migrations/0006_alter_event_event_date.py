# Generated by Django 3.2.9 on 2022-12-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leaderboard", "0005_alter_event_event_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event_date",
            field=models.DateField(help_text="Day of the event"),
        ),
    ]

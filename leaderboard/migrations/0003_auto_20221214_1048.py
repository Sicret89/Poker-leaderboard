# Generated by Django 3.2.9 on 2022-12-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_auto_20221213_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='E10B',
            new_name='E10B_47',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E11B',
            new_name='E10B_AK',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E12B',
            new_name='E11B_47',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E1B',
            new_name='E11B_AK',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E2B',
            new_name='E12B_47',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E3B',
            new_name='E12B_AK',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E4B',
            new_name='E1B_47',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E5B',
            new_name='E1B_AK',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E6B',
            new_name='E2B_47',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E7B',
            new_name='E2B_AK',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E8B',
            new_name='E3B_47',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='E9B',
            new_name='E3B_AK',
        ),
        migrations.AddField(
            model_name='player',
            name='E4B_47',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E4B_AK',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E5B_47',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E5B_AK',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E6B_47',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E6B_AK',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E7B_47',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E7B_AK',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E8B_47',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E8B_AK',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E9B_47',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='E9B_AK',
            field=models.IntegerField(default=0),
        ),
    ]

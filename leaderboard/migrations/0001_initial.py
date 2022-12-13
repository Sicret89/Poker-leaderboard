# Generated by Django 3.2.9 on 2022-12-13 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('E1', models.IntegerField(default=0)),
                ('E2', models.IntegerField(default=0)),
                ('E3', models.IntegerField(default=0)),
                ('E4', models.IntegerField(default=0)),
                ('E5', models.IntegerField(default=0)),
                ('E6', models.IntegerField(default=0)),
                ('E7', models.IntegerField(default=0)),
                ('E8', models.IntegerField(default=0)),
                ('E9', models.IntegerField(default=0)),
                ('E10', models.IntegerField(default=0)),
                ('E11', models.IntegerField(default=0)),
                ('E12', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_prize', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 2.0.1 on 2018-04-28 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]

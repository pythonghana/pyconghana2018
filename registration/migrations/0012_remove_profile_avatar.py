# Generated by Django 2.0.1 on 2018-05-01 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]

# Generated by Django 2.0.1 on 2018-04-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20180428_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profile/avatar.jpg', max_length=255, null=True, upload_to='profile/avatars/'),
        ),
    ]
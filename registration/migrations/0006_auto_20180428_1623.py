# Generated by Django 2.0.1 on 2018-04-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20180428_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='', max_length=255, null=True, upload_to='media/avatar/'),
        ),
    ]

# Generated by Django 2.0.1 on 2018-03-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20180307_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
# Generated by Django 2.0.1 on 2018-04-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0005_auto_20180418_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='url',
            field=models.URLField(blank=True, default='', help_text='Link to Photo Ablum'),
        ),
    ]

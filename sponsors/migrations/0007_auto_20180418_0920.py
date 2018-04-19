# Generated by Django 2.0.1 on 2018-04-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0006_sponsor_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='website',
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='url',
            field=models.URLField(blank=True, default='', help_text='Link to Sponsor website'),
        ),
    ]
# Generated by Django 2.0.1 on 2018-04-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_auto_20180307_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='website',
            field=models.URLField(blank=True, default='', help_text='website URL/ Twitter handle', null=True),
        ),
    ]

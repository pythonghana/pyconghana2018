# Generated by Django 2.0.1 on 2018-04-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0016_auto_20180419_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='talk_type',
            field=models.CharField(choices=[('Short Talk', 'Short Talk - 30 mins'), ('Long Talk', 'Longnote Talk - 45 mins')], max_length=20),
        ),
    ]

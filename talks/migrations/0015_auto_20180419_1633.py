# Generated by Django 2.0.1 on 2018-04-19 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0014_auto_20180419_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='programming_experience',
            new_name='intended_audience',
        ),
    ]

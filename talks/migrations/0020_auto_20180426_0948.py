# Generated by Django 2.0.1 on 2018-04-26 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0019_auto_20180426_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='email',
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='url',
        ),
    ]
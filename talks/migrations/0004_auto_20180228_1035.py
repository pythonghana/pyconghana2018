# Generated by Django 2.0.1 on 2018-02-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0003_proposal_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='image',
        ),
        migrations.AddField(
            model_name='proposal',
            name='email',
            field=models.EmailField(default='', help_text='We’ll keep it secret, for internal use only.', max_length=1024),
        ),
        migrations.AddField(
            model_name='proposal',
            name='extra_requirement',
            field=models.TextField(blank=True, default='', help_text='Anything else you want to tell us?.', null=True),
        ),
        migrations.AddField(
            model_name='proposal',
            name='name',
            field=models.CharField(default='', help_text='Your name', max_length=1024),
        ),
        migrations.AddField(
            model_name='proposal',
            name='url',
            field=models.URLField(default='', help_text='Got a video?'),
        ),
    ]

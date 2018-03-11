# Generated by Django 2.0.1 on 2018-03-01 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(blank=True, help_text='Your photo (not an illustration nor avatar), It will be published on the website. Ideal photo is: a head shot, shows only you, has no “filters” applied and is as large and uncompressed as possible. We might crop it and change contrast, brightness etc. to fit our visual style.', null=True, upload_to='speakers')),
                ('bio', models.TextField(help_text='Tell us a bit about yourself and your work with Python', max_length=500)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('birth_date', models.DateField(blank=True, help_text='YYYY-MM-DD', null=True)),
                ('contact_number', models.CharField(help_text='Please include your country code.', max_length=16, null=True)),
                ('website', models.CharField(blank=True, help_text='Your website/blog URL.', max_length=255, null=True)),
                ('twitter_handle', models.CharField(blank=True, max_length=15, null=True)),
                ('github_username', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=40, verbose_name='activation key')),
                ('activated', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'registration profile',
                'verbose_name_plural': 'registration profiles',
            },
        ),
        migrations.CreateModel(
            name='SupervisedRegistrationProfile',
            fields=[
                ('registrationprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registration.RegistrationProfile')),
            ],
            bases=('registration.registrationprofile',),
        ),
        migrations.AddField(
            model_name='registrationprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
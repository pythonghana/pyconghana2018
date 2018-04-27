from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Proposal(models.Model):
    TALK_TYPES = (
        ('Short Talk', "Short Talk - 30 mins"),
        ('Long Talk', "Long Talk - 45 mins"),
    )

    STATUS = (('S', 'Submitted'),
              ('A', 'Accepted'),
              ('W', 'Waiting List'),
              ('R', 'Rejected'),)

    PROGRAMMING_EXPERIENCE = (('BP','Beginners'),
                        ('IP', 'Intermediate Programmers'),
                        ('EP', 'Expert Programmers'))


    title = models.CharField(  help_text="Public title. What topic/project is it all about?", max_length=1024)
    talk_type = models.CharField(choices=TALK_TYPES, max_length=20)
    proposal_id = models.AutoField(primary_key=True, default=None)
    Tell_the_audience_about_your_talk = models.TextField(max_length=255, help_text = "Describe your Talk to your targeted audience . Please include the requirements: libraries and Python version to be installed, required experience with topics/libraries, etc.", blank=False)
    abstract = models.TextField(default='', help_text = "Your Abstract.", blank=True, null=True
                             )
    user = models.ForeignKey(User, related_name="proposals", default='', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=1, default='S')
    intended_audience = models.CharField(choices=PROGRAMMING_EXPERIENCE, help_text = "Your targeted audience.", max_length=30, default='')
    Anything_else_you_want_to_tell_us = models.TextField(default='', help_text = "Kindly add anything else you want to tell us?.", blank=True, null=True)
    recording_release = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Proposal(models.Model):
    TALK_TYPES = (
        ('Short Talk', "Short Talk - 30 mins"),
        ('Long Talk', "Long Talk - 1 hour"),
        ('Keynote', "Keynote Talk - 45 mins"),
    )

    STATUS = (('S', 'Submitted'),
              ('A', 'Accepted'),
              ('W', 'Waiting List'),
              ('R', 'Rejected'),)

    PROGRAMMING_EXPERIENCE = (('BP','Beginners'),
                        ('IP', 'Intermediate Programmers'),
                        ('SP', 'Senior Programmers'),
                        ('EP', 'Expert Programmers'))

    
    email = models.EmailField(max_length=1024, default='', help_text = "We’ll keep it secret, for internal use only.")
    title = models.CharField(  help_text="Public title. What topic/project is it all about?", max_length=1024)
    talk_type = models.CharField(choices=TALK_TYPES, max_length=20)
    proposal_id = models.AutoField(primary_key=True, default=None)
    Tell_the_audience_about_your_talk = models.TextField(max_length=255, help_text = "Describe your workshop or sprint. Please include the requirements: libraries and Python version to be installed, required experience with topics/libraries, etc.", blank=False)
    url = models.URLField(default='', help_text='Got a video? If you have a recording of you giving a talk or leading a workshop, you can paste the link here.')
    notes = models.TextField(default='', help_text = "Other Informations.", blank=True, null=True
                             )
    user = models.ForeignKey(User, related_name="proposals", default='', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=1, default='')
    programming_experience = models.CharField(choices=PROGRAMMING_EXPERIENCE, help_text = "Your targeted audience.", max_length=30, default='')
    Anything_else_you_want_to_tell_us = models.TextField(default='', help_text = "Kindly add anything else you want to tell us?.", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
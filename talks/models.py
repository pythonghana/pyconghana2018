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

    title = models.CharField(max_length=1024)
    talk_type = models.CharField(choices=TALK_TYPES, max_length=20)
    proposal_id = models.AutoField(primary_key=True, default=None)
    proposal = models.CharField(max_length=255, blank=False)
    notes = models.TextField(default='', help_text = "Other Informations.", blank=True, null=True
                             )
    user = models.ForeignKey(User, related_name="proposals", default='', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=1, default='')
    programming_experience = models.CharField(choices=PROGRAMMING_EXPERIENCE, max_length=30, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
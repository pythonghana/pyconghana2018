from django.db import models


class Sponsor(models.Model):
    SPONSOR_PACKAGES = (('Bronze', 'Bronze - $500'),
                        ('Silver', 'Silver - $1000'),
                        ('Gold', 'Gold - $2500'),
                        ('Diamond', 'Diamond - $3500'),
                        ('Other', 'Other'),
                        )

    SPONSOR_TYPE =(('C', 'Corporate Sponsor'),
                   ('I', 'Individual Sponsor'),)

    name = models.CharField("sponsor name", max_length=200)
    category = models.CharField(max_length=15, choices=SPONSOR_PACKAGES)
    logo = models.ImageField(max_length=255, blank=True, null=True)
    type = models.CharField("sponsor type", max_length=1, choices=SPONSOR_TYPE)
    url = models.URLField(default='', help_text='Link to Sponsor website', blank=True,)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


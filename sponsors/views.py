from __future__ import absolute_import
from django.shortcuts import render, reverse
from .models import Sponsor
from django.http import HttpRequest, HttpResponseRedirect

# Create your views here.

from django.shortcuts import render, redirect
from django.conf import settings

from datetime import datetime

from rest_framework import viewsets

from .models import Sponsor
from .forms import SponsorForm


def Prospectus(request):
    context = {}
    template = 'prospectus.html'
    return render(request, template, context)



def sponsors(request):
    assert isinstance(request, HttpRequest)
    diamond = Sponsor.objects.filter(category="Diamond")
    gold = Sponsor.objects.filter(category="Gold")
    silver = Sponsor.objects.filter(category="Silver")
    bronze = Sponsor.objects.filter(category="Bronze")
    individuals = Sponsor.objects.filter(type="I")

    return render(
        request,
        'sponsors/sponsors.html',
        {

            'diamond': diamond,
            'gold': gold,
            'silver': silver,
            'bronze': bronze,
            'individuals': individuals,
        }
    )

def apply(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        form = SponsorForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Sponsor()  # gets new object'sponsor_name', 'contact_name', 'contact_email', 'category', 'type', 'url'
            obj.sponsor_name = form.cleaned_data['sponsor_name']
            obj.contact_name = form.cleaned_data['contact_name']
            obj.contact_email = form.cleaned_data['contact_email']
            obj.category = form.cleaned_data['category']
            obj.type = form.cleaned_data['type']
            obj.sponsor_url = form.cleaned_data['sponsor_url']
            # finally save the object in db
            obj.save()

            return HttpResponseRedirect(reverse('sponsor:submit'))

    else:
        form = SponsorForm()

        return render(
            request,
            "sponsors/sponsors_form.html",
            {
                'title': 'Apply for Sponsorship',
                'year': datetime.now().year,
                'form': form,
            }
        )


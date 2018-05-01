from __future__ import absolute_import
from django.shortcuts import render, reverse
from .models import Sponsor
from django.http import HttpRequest, HttpResponseRedirect

# Create your views here.


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
    special = Sponsor.objects.filter(category="Special")
    individuals = Sponsor.objects.filter(type="I")

    return render(
        request,
        'sponsors/sponsors.html',
        {

            'diamond': diamond,
            'gold': gold,
            'silver': silver,
            'bronze': bronze,
            'special': special,
            'individuals': individuals,
        }
    )

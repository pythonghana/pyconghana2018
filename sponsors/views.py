from django.shortcuts import render

# Create your views here.


def sponsors(request):
    context = {}
    template = 'sponsors.html'
    return render(request, template, context)


def Prospectus(request):
    context = {}
    template = 'prospectus.html'
    return render(request, template, context)
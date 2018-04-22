from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.


def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)


def page_not_found(request):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)
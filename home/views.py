from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.


def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def handler404(request, exception):
    return render(request, '404.html', locals())
from django.shortcuts import render
from django.shortcuts import (
render_to_response
)
from django.template import RequestContext


# Create your views here.
def privacypolicy(request):
    context = {}
    template = 'privacypolicy.html'
    return render(request, template, context)
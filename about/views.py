from django.shortcuts import render
from django.shortcuts import (
render_to_response
)
from django.template import RequestContext


# Create your views here.
def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)
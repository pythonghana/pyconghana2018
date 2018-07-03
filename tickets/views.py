from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import (
render_to_response
)
from django.template import RequestContext


# Create your views here.
def ticket(request):
    context = {}
    template = 'ticket/ticket.html'
    return render(request, template, context)

def register(request):
    context = {}
    template = 'ticket/register.html'
    return render(request, template, context)
from django.shortcuts import render
from django.shortcuts import (
render_to_response
)
from django.template import RequestContext


# Create your views here.
def faqs(request):
    context = {}
    template = 'faq.html'
    return render(request, template, context)
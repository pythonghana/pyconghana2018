from django.shortcuts import render

# Create your views here.


def support_us(request):
    context = {}
    template = 'support_us.html'
    return render(request, template, context)
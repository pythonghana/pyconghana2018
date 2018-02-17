from django.shortcuts import render

# Create your views here.


def schedule(request):
    context = {}
    template = 'schedule.html'
    return render(request, template, context)

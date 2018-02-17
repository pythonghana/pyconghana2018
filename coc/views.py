from django.shortcuts import render

# Create your views here.


def coc(request):
    context = {}
    template = 'coc.html'
    return render(request, template, context)

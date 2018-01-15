from django.shortcuts import render


# Create your views here.
def talks(request):
    context = {}
    template = 'talks.html'
    return render(request, template, context)

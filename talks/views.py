from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, UpdateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from datetime import datetime

from rest_framework import viewsets

from .serializers import TalkSerializer
from .models import Proposal
from .models import Document
from .forms import DocumentForm
from .forms import ProposalForm
from .mixins import EditOwnTalksMixin



@login_required
def submit_talk(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        form = ProposalForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Proposal()  # gets new object
            obj.user_id = request.user.pk
            obj.username = request.user.username
            obj.email = form.cleaned_data['email']
            obj.title = form.cleaned_data['title']
            obj.Tell_the_audience_about_your_talk = form.cleaned_data['Tell_the_audience_about_your_talk']
            obj.talk_type = form.cleaned_data['talk_type']
            obj.intended_audience = form.cleaned_data['intended_audience']
            obj.abstract = form.cleaned_data['abstract']
            # finally save the object in db
            obj.save()
            subject = "[PyCon Ghana 2018] Talk Successfully Submitted"
            message = '''\nDear {},
                        \nYour talk to PyConGhana 2018 was Successfully Submitted. Thank You!
                        \n
                        \n
                        \nThese are the overview of your Submission:
                        \nTalk Title: {} 
                        \nTalk Type: {} 
                        \nIntended Audience: {}  
                        \nTalk Description: {} 
                        \nAbstract: {}
                        \n
                        \n
                        \nSincerely, 
                        \nPycon Ghana Management.
                        '''.format(obj.username, obj.title, obj.talk_type, obj.intended_audience, obj.Tell_the_audience_about_your_talk, obj.abstract)
            try:
                send_mail(subject, message,'noreply@gh.pycon.org', [obj.email, ])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return HttpResponseRedirect(reverse('talks:submitted'))

    else:
        form = ProposalForm()

        return render(
            request,
            "talks/talk_form.html",
            {
                'title': 'Submit a Talk',
                'year': datetime.now().year,
                'form': form,
            }
        )


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


class TalkList(TemplateView):
    template_name = "talks/talk_list.html"

    def get_context_data(self, **kwargs):
        context = super(TalkList, self).get_context_data(**kwargs)
        context['title'] = "Submitted Talks"
        context['year'] = datetime.now().year
        context['submitted_talks'] = Proposal.objects.filter(user=self.request.user.pk)
        return context


class TalkView(EditOwnTalksMixin, UpdateView):
    template_name = "talks/talk.html"
    form_class = ProposalForm
    model = Proposal
    success_url = reverse_lazy('talks:submitted')

    def get_context_data(self, **kwargs):
        context = super(TalkView, self).get_context_data(**kwargs)
        context['title'] = "Talk Details"
        context['year'] = datetime.now().year
        context['talk'] = get_object_or_404(Proposal, pk=self.kwargs['pk'])
        return context


class SuccessView(TemplateView):
    template_name = "talks/success.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['title'] = 'Talk Submission Successful'
        context['year'] = datetime.now().year
        return context


class TalkViewsSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = TalkSerializer
    queryset = Proposal.objects.all()


class AcceptedTalksView(TemplateView):
    template_name = "talks/accepted_talks.html"

    def get_context_data(self, **kwargs):
        context = super(AcceptedTalksView, self).get_context_data(**kwargs)
        context['title'] = "Accepted Talks"
        context['year'] = datetime.now().year
        talks_list = Proposal.objects.filter(status='A').select_related('user')

        paginator = Paginator(talks_list, 10)  # Show 10 posts per page
        page = self.request.GET.get('page')
        try:
            accepted_talks = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            accepted_talks = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            accepted_talks = paginator.page(paginator.num_pages)
        context['accepted_talks'] = accepted_talks
        return context


class TalkDetailView(TemplateView):
    template_name = "talks/talk_details.html"

    def get_context_data(self, **kwargs):
        context = super(TalkDetailView, self).get_context_data(**kwargs)
        context['title'] = "Accepted Talks"
        context['year'] = datetime.now().year
        context['talk'] = Proposal.objects.get(pk=self.kwargs['pk'])
        return context


def home(request):
    documents = Document.objects.all()
    return render(request, 'upload/home.html', { 'documents': documents })

def submit(request):
    context = {}
    template = 'talks/talks.html'
    return render(request, template, context)

def recording(request):
    context = {}
    template = 'talks/recordings.html'
    return render(request, template, context)

def proposing(request):
    context = {}
    template = 'talks/proposing_a_talk.html'
    return render(request, template, context)

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload/model_form_upload.html', {
        'form': form
    })

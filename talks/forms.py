from talks.models import Proposal
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Document
from captcha.fields import ReCaptchaField


class ProposalForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Proposal
        fields = ('email','title', 'talk_type', 'intended_audience', 'Tell_the_audience_about_your_talk', 'abstract', 'Anything_else_you_want_to_tell_us', 'recording_release',)

    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'


class DocumentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Document
        fields = ('description', 'document', )

from talks.models import Proposal
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Document


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ('email', 'title', 'Tell_the_audience_about_your_talk', 'programming_experience', 'notes', 'talk_type', 'Anything_else_you_want_to_tell_us',)

    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
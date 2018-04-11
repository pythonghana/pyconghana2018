from talks.models import Proposal
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Document
from captcha.fields import ReCaptchaField


class ProposalForm(forms.ModelForm):
    captcha = ReCaptchaField(
        public_key='6Ldbq1IUAAAAAGLKryi-oZs8tE1D4DAXQx6hFzAf',
        private_key='6Ldbq1IUAAAAABhyiq30Ur9ySQgsM_Mnc7rNk3Y7',
    )

    class Meta:
        model = Proposal
        fields = ('email', 'title', 'Tell_the_audience_about_your_talk', 'programming_experience', 'notes', 'talk_type', 'Anything_else_you_want_to_tell_us',)

    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'


class DocumentForm(forms.ModelForm):
    captcha = ReCaptchaField(
        public_key='6Ldbq1IUAAAAAGLKryi-oZs8tE1D4DAXQx6hFzAf',
        private_key='6Ldbq1IUAAAAABhyiq30Ur9ySQgsM_Mnc7rNk3Y7',
    )

    class Meta:
        model = Document
        fields = ('description', 'document', )

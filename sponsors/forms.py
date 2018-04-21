from sponsors.models import Sponsor
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from captcha.fields import ReCaptchaField


class SponsorForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Sponsor
        fields = ('sponsor_name', 'contact_name', 'contact_email', 'category', 'type', 'sponsor_url')

    def __init__(self, *args, **kwargs):
        super(SponsorForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'

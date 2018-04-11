from __future__ import unicode_literals
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _
from .users import UserModel
from .users import UsernameField
from captcha.fields import ReCaptchaField

User = UserModel()


class RegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    required_css_class = 'required'
    email = forms.EmailField(label=_("E-mail"))
    captcha = ReCaptchaField(
        public_key='6Ldbq1IUAAAAAGLKryi-oZs8tE1D4DAXQx6hFzAf',
        private_key='6Ldbq1IUAAAAABhyiq30Ur9ySQgsM_Mnc7rNk3Y7',
    )

    class Meta:
        model = User
        fields = (UsernameField(), "email")


class RegistrationFormUsernameLowercase(RegistrationForm):
    """
    A subclass of :class:`RegistrationForm` which enforces unique case insensitive
    usernames, make all usernames to lower case.

    """
    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()
        if User.objects.filter(**{UsernameField(): username}).exists():
            raise forms.ValidationError(_('A user with that username already exists.'))

        return username


class RegistrationFormTermsOfService(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.

    """
    tos = forms.BooleanField(widget=forms.CheckboxInput,
                             label=_('I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})


class RegistrationFormUniqueEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.

    """
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


class RegistrationFormNoFreeEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which disallows registration with
    email addresses from popular free webmail services; moderately
    useful for preventing automated spam registrations.

    To change the list of banned domains, subclass this form and
    override the attribute ``bad_domains``.

    """
    bad_domains = ['aim.com', 'msn.com', 'mail.ru']

    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.

        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free email addresses is prohibited. Please supply a different email address."))
        return self.cleaned_data['email']


class ResendActivationForm(forms.Form):
    required_css_class = 'required'
    email = forms.EmailField(label=_("E-mail"))


class UpdateForm(forms.ModelForm):
    captcha = ReCaptchaField(
        public_key='6Ldbq1IUAAAAAGLKryi-oZs8tE1D4DAXQx6hFzAf',
        private_key='6Ldbq1IUAAAAABhyiq30Ur9ySQgsM_Mnc7rNk3Y7',
    )
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'image_url', 'bio', 'twitter_handle', 'github_username', 'contact_number', 'website', 'city', 'country',)

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_UpdateForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('update', 'Update Profile'))


class UserForm(forms.ModelForm):
    captcha = ReCaptchaField(
        public_key='6Ldbq1IUAAAAAGLKryi-oZs8tE1D4DAXQx6hFzAf',
        private_key='6Ldbq1IUAAAAABhyiq30Ur9ySQgsM_Mnc7rNk3Y7',
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_UserForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('update', 'Update Profile'))


class PasswordForm(PasswordChangeForm):
    captcha = ReCaptchaField(
        public_key='6Ldbq1IUAAAAAGLKryi-oZs8tE1D4DAXQx6hFzAf',
        private_key='6Ldbq1IUAAAAABhyiq30Ur9ySQgsM_Mnc7rNk3Y7',
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_UserForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.Layout(
            'old_password',
            'password1',
            'password2'
        )
        self.helper.add_input(Submit('update', 'Update Profile'))

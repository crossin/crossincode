from django import forms
from registration.forms import RegistrationFormUniqueEmail


class RegistrationForm(RegistrationFormUniqueEmail):
    # limits length of username/password.

    def clean_username(self):
        # < 30 chars
        username = super(RegistrationForm, self).clean_username()
        if len(username) >= 30:
            raise forms.ValidationError("Your username is too long.")
        else:
            return username

    def clean_password1(self):
        # >= 6 chars & <= 30 chars
        pwd = self.cleaned_data['password1']
        print len(pwd)
        if len(pwd) < 6:
            raise forms.ValidationError("Your password is too short.")
        elif len(pwd) > 30:
            raise forms.ValidationError("Your password is too long.")
        else:
            return pwd

from django import forms
from account.forms import SignupForm

CHOICES = (('work', 'Work'), ('hire', 'Hire'))

class CustomSignupForm(SignupForm):
    acc_type = forms.ChoiceField(widget=forms.Select,
                                 choices=CHOICES,
                                 label='I want to'
    )
    first_name = forms.CharField(widget=forms.TextInput,
                                 label='First name',
                                 required=True
    )
    last_name = forms.CharField(widget=forms.TextInput,
                                 label='Last name',
                                 required=True
    )
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    def save(self, *args, **kwargs):
        user = super(SignupForm, self).save(*args, **kwar)

        return user

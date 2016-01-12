from django import forms
from account.forms import SettingsForm
from datetime import datetime
from django.forms.extras.widgets import SelectDateWidget

from custom_settings import models
from custom_reg.models import Skill

from cities_light.models import Country, City

import custom_reg.labels as labels

years = [(str(x), str(x)) for x in range(1980, datetime.today().year+1)]
currencies = [('euro', 'EUR'), ('dollar', 'USD'),
              ('kronor', 'SEK'), ('taiwan dollar', 'TWD'),
              ('hong kong dollar', 'HKD')]

class PersonalSettingsForm(SettingsForm):


    first_name = forms.CharField(widget=forms.TextInput,
                                 label='First name',
                                 required=True
    )

    last_name = forms.CharField(widget=forms.TextInput,
                                 label='Last name',
                                 required=True
    )


    countries = [(x.id, x.name) for x in Country.objects.all()]
    countries.insert(0, (-1, '----------'))
    country = forms.ChoiceField(choices=countries,
                                label='Country',
                                required=False
    )

    city = forms.CharField(widget=forms.Select,
                           label='City',
                           required=False
    )

    salary_amount = forms.CharField(widget=forms.TextInput,
                                    label='Minimum salary rate',
                                    required=False
    )

    salary_currency = forms.ChoiceField(required=False,
                                        choices=currencies
    )

    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        if 'timezone' in self.fields:
            del self.fields['timezone']
        if 'language' in self.fields:
            del self.fields['language']

class WorkerIntroForm(forms.Form):
    intro = forms.CharField(widget=forms.Textarea(attrs={'placeholder': labels.INTRO_INITIAL}),
                            label=labels.INTRO_LABEL,
                            required=False,
    )

class WorkerSkillForm(forms.ModelForm):
    skill = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Skill
        fields = ('skill',)

class ClientSettingsForm(forms.Form):
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': labels.SKILLS_INITIAL}),
                             label=labels.SKILLS_LABEL,
                             required=False,
    )

class WorkExperienceForm(forms.ModelForm):
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company'}),
                           required=True,
    )
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}),
                           required=True,
    )
    from_year = forms.ChoiceField(required=False,
                                  label='From',
                                  choices=years,
    )
    to_year = forms.ChoiceField(required=False,
                                label='To',
                                choices=years,
    )

    class Meta:
        model = models.WorkExperience
        fields = ('company', 'title', 'from_year', 'to_year')

class EducationForm(forms.ModelForm):
    school = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'School'}),
                             required=True
    )
    programme = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Programme'}),
                             required=True
    )
    from_year = forms.ChoiceField(label='From',
                                  choices=years,
    )
    to_year = forms.ChoiceField(label='To',
                                choices=years,
    )

    class Meta:
        model = models.Education
        fields = ('school', 'programme', 'from_year', 'to_year')

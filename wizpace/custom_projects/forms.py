from django import forms

from models import Project
from custom_reg.models import Skill

class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for fieldname in ['skills']:
            self.fields[fieldname].help_text = "Add the skills you require."

    title = forms.CharField(widget=forms.TextInput,
                            label='Title',
                            required=True)

    description = forms.CharField(widget=forms.Textarea,
                                  label='Description',
                                  required=True)

    skills = forms.CharField(widget=forms.SelectMultiple,
                             label='Skills',
                             required=True)

    nr_of_workers = forms.ChoiceField(label='Required workers',
                                      choices=[(str(x), x) for x in range(1,11)],
                                      required=True)

    end_date = forms.CharField(widget=forms.TextInput,
                               label='Completion date',
                               required=True)

    class Meta:
        model = Project
        fields = ('title', 'description', 'skills')
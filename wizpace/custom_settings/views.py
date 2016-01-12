import django.views.generic.edit as django_views
import account.views as account_views

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse

from account.models import EmailAddress
from account.conf import settings
from cities_light.models import City, Country

from custom_settings.forms import PersonalSettingsForm, WorkerIntroForm, ClientSettingsForm, WorkExperienceForm, WorkerSkillForm, EducationForm
from custom_settings.models import WorkExperience, Education
from custom_reg.models import Skill
from custom_views import PermissionMixin

from itertools import chain

class PasswordChangeView(account_views.ChangePasswordView):
    template_name = 'custom_settings/password_change.html'

class DeleteView(account_views.DeleteView):
    template_name = 'custom_settings/delete.html'

class PersonalSettingsView(django_views.FormView):
    template_name = 'custom_settings/settings_personal.html'
    form_class = PersonalSettingsForm
    is_worker = True
    messages = {
        "settings_updated": {
            "level": messages.SUCCESS,
            "text": ("Personal information updated.")
        },
        "settings_invalid": {
            "level": messages.ERROR,
            "text": ("Your submission was not saved, please try again.")
        },
        "request_invalid": {
            "level": messages.WARNING,
            "text": ("Invalid request.")
        },
    }

    success_url = reverse_lazy('account_personal')

    def get(self, *args, **kwargs):
        if hasattr(self.request.user, 'client_profile'):
            self.is_worker = False
        return super(PersonalSettingsView, self).get(*args, **kwargs)

    def get_form_class(self):
        # @@@ django: this is a workaround to not having a dedicated method
        # to initialize self with a request in a known good state (of course
        # this only works with a FormView)
        return super(PersonalSettingsView, self).get_form_class()

    def get_initial(self):
        initial = {}
        if self.is_worker:
            return self.get_worker_initial(initial)
        else:
            return self.get_client_initial(initial)

    def get_worker_initial(self, initial):
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email
        if self.request.user.worker_profile:
            profile = self.request.user.worker_profile
        else:
            profile = self.request.user.client_profile
        if profile.country:
            initial['country'] = profile.country.id
        return initial

    def get_client_initial(self, initial):
        return initial

    def form_valid(self, form):
        self.update_settings(form)
        msg = self.messages["settings_updated"]
        messages.add_message(
            self.request,
            msg["level"],
            msg["text"]
        )
        return super(PersonalSettingsView, self).form_valid(form)

    def form_invalid(self, form):
        msg = self.messages["settings_invalid"]
        messages.add_message(
            self.request,
            msg["level"],
            msg["text"]
        )
        return super(PersonalSettingsView, self).form_invalid(form)

    def update_settings(self, form):
        self.update_user(form)
        self.update_email(form)
        if self.is_worker:
            self.update_worker_profile(form)
        else:
            self.update_client_profile(form)

    def update_email(self, form, confirm=None):
        user = self.request.user
        email = form.cleaned_data["email"].strip()
        user.email = email
        user.username = email
        user.save()

    def update_user(self, form):
        fields = {}
        if 'first_name' in form.cleaned_data:
            fields['first_name'] = form.cleaned_data['first_name']
        if 'last_name' in form.cleaned_data:
            fields['last_name'] = form.cleaned_data['last_name']
        if fields:
            for k, v in fields.items():
                setattr(self.request.user, k, v)
            self.request.user.save()

    def update_worker_profile(self, form):
        fields = {}
        profile = self.request.user.worker_profile
        if 'intro' in form.cleaned_data:
            fields['intro'] = form.cleaned_data['intro']
        if 'skills' in form.cleaned_data:
            fields['skills'] = form.cleaned_data['skills']
        if 'country' in form.cleaned_data:
            if '-' not in form.cleaned_data['country']:
                country = Country.objects.get(id=form.cleaned_data['country'])
                profile.country = country
                profile.save()
            else:
                profile.country = None
                profile.save()
        if fields:
            for k, v in fields.items():
                setattr(profile, k, v)
            profile.save()

    def update_client_profile(self, form):
        pass

# Custom function-based views

@login_required
def experience_view(request):
    context_dict = {}
    if request.method == 'POST':
        if 'company' in request.POST:
            form = WorkExperienceForm(request.POST)
            if form.is_valid():
                experience, created = WorkExperience.objects.get_or_create(
                    company=form.cleaned_data['company'],
                    title=form.cleaned_data['title'],
                    from_year=form.cleaned_data['from_year'],
                    to_year=form.cleaned_data['to_year'],
                    user_id=request.user.id
                    )
                if not created:
                    messages.add_message(request, messages.WARNING, 'Work experience already present.')
                else:
                    experience.user = request.user
                    experience.save()
                    messages.add_message(request, messages.SUCCESS, 'Work experience added.')
        elif 'school' in request.POST:
            form = EducationForm(request.POST)
            if form.is_valid():
                education, created = Education.objects.get_or_create(
                    school=form.cleaned_data['school'],
                    programme=form.cleaned_data['programme'],
                    from_year=form.cleaned_data['from_year'],
                    to_year=form.cleaned_data['to_year'],
                    user_id=request.user.id
                    )
                if not created:
                    messages.add_message(request, messages.WARNING, 'Education information already present.')
                else:
                    education.user = request.user
                    education.save()
                    messages.add_message(request, messages.SUCCESS, 'Education information added.')
        return redirect(reverse_lazy('account_experience'))
    else:
        exp_form = WorkExperienceForm()
        edu_form = EducationForm()
        context_dict['exp_form'] = exp_form
        context_dict['edu_form'] = edu_form

    return render(request, 'custom_settings/settings_experience.html', context_dict)

@login_required
def self_intro_view(request):
    if request.method == 'POST':
        if 'intro' in request.POST:
            form = WorkerIntroForm(request.POST)
            if form.is_valid():
                setattr(request.user.worker_profile, 'intro', form.cleaned_data['intro'])
                request.user.worker_profile.save()
                messages.add_message(request, messages.SUCCESS, 'Self introduction updated.')
        elif 'skill' in request.POST:
            form = WorkerSkillForm(request.POST)
            if form.is_valid():
                skill, created = Skill.objects.get_or_create(name=form.cleaned_data['skill'].lower())
                if created:
                    skill.save()
                if skill not in request.user.worker_profile.skills.all():
                    request.user.worker_profile.skills.add(skill)
                    request.user.worker_profile.save()
                    messages.add_message(request, messages.SUCCESS, 'Skill added.')
                else:
                    messages.add_message(request, messages.ERROR, 'Skill already present.')
        return redirect(reverse_lazy('account_intro'))
    else:
        if request.user.worker_profile.intro:
            intro_form = WorkerIntroForm(initial={'intro': request.user.worker_profile.intro, })
        else:
            intro_form = WorkerIntroForm()
        skills_form = WorkerSkillForm()
        context_dict = {'intro_form': intro_form, 'skills_form': skills_form}
        return render(request, 'custom_settings/settings_intro.html', context_dict)

# Delete Views

class ExperienceDelete(PermissionMixin, django_views.DeleteView):
    model = WorkExperience
    success_url = reverse_lazy('account_experience')
    success_message = "Work experience deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ExperienceDelete, self).delete(request, *args, **kwargs)

class EducationDelete(PermissionMixin, django_views.DeleteView):
    model = Education
    success_url = reverse_lazy('account_experience')
    success_message = "Education information deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EducationDelete, self).delete(request, *args, **kwargs)

class SkillDelete(django_views.DeleteView):
    model = Skill
    success_url = reverse_lazy('account_intro')
    success_message = "Skill deleted."

    def delete(self, request, *args, **kwargs):
        skill = get_object_or_404(Skill, pk=kwargs['pk'])
        request.user.worker_profile.skills.remove(skill)
        skill.workerprofile_set.remove(request.user.worker_profile)
        messages.success(self.request, self.success_message)
        return redirect(self.success_url)

def search_city(request):
    query = request.GET.get('q', '')
    country = request.GET.get('country', '')
    user_country = Country.objects.get(name=country)
    cities1 = City.objects.filter(name__contains=query, country=user_country)
    cities2 = City.objects.filter(name__contains=query.title(), country=user_country)
    cities = list(chain(cities1, cities2))
    json_dicts = []
    for city in cities:
        obj_dict = {}
        obj_dict['id'] = city.id
        obj_dict['name'] = city.name
        json_dicts.append(obj_dict)
    return JsonResponse(data=json_dicts, safe=False)
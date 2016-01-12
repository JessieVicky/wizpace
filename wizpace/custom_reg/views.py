from django.contrib.auth.models import Group

from account.views import SignupView, LoginView

from account.forms import LoginEmailForm

from custom_reg.models import WorkerProfile, ClientProfile
from custom_reg.forms import CustomSignupForm

class LoginView(LoginView):
    form_class = LoginEmailForm

class SignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'custom_reg/signup.html'

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        username = form.cleaned_data['email']
        return username

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup(form)

    def create_profile(self, form):
        self.created_user.first_name = form.cleaned_data['first_name']
        self.created_user.last_name = form.cleaned_data['last_name']
        self.created_user.save()
        if form.cleaned_data['acc_type'] == u'work':
            profile = WorkerProfile(user=self.created_user)
            self.created_user.groups.add(Group.objects.get(name='Freelancers'))
        else:
            profile = ClientProfile(user=self.created_user)
            self.created_user.groups.add(Group.objects.get(name='Clients'))
        profile.save()
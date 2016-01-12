from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.list import ListView

from custom_reg.models import WorkerProfile

class TalentsListView(ListView):
    model = User
    template_name = 'user_profiles/list.html'

    def get_context_data(self, **kwargs):
        context = super(TalentsListView,self).get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(groups__name='Freelancers')
        return context

@login_required
def profile_detail(request, uuid):
    profile = WorkerProfile.objects.get(uuid=uuid)
    context_dict = {'user': profile.user}
    return render(request, 'user_profiles/profile_overview.html', context_dict)

@login_required
def profile_detail_experience(request, uuid):
    profile = WorkerProfile.objects.get(uuid=uuid)
    context_dict = {'user': profile.user}
    return render(request, 'user_profiles/profile_exp.html', context_dict)

@login_required
def profile_detail_portfolio(request, uuid):
    profile = WorkerProfile.objects.get(uuid=uuid)
    context_dict = {'user': profile.user}
    return render(request, 'user_profiles/profile_portfolio.html', context_dict)
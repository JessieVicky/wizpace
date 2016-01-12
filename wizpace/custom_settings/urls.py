from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from custom_settings import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^personal/search_city/$', views.search_city, name='settings_search_city'),
    url(r'^personal/', login_required(views.PersonalSettingsView.as_view()), name='account_personal'),
    url(r'^intro/delete_skill/(?P<pk>\d+)/$', login_required(views.SkillDelete.as_view()) , name='account_skill_delete'),
    url(r'^intro/', views.self_intro_view, name='account_intro'),
    url(r'^experience/delete_exp/(?P<pk>\d+)/$', login_required(views.ExperienceDelete.as_view()), name='account_experience_delete'),
    url(r'^experience/delete_edu/(?P<pk>\d+)/$', login_required(views.EducationDelete.as_view()), name='account_education_delete'),
    url(r'^experience/', views.experience_view, name='account_experience'),
    url(r'^password/', login_required(views.PasswordChangeView.as_view()), name='account_password'),
    url(r'^delete/', login_required(views.DeleteView.as_view()), name='account_delete'),
)

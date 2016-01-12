from django.conf.urls import patterns, url

from user_profiles import views

urlpatterns = patterns('',
    url(r'^list/', views.TalentsListView.as_view(), name='profiles_list'),
    url(r'^(?P<uuid>[\w-]+)/experience', views.profile_detail_experience, name='profile_detail_experience'),
    url(r'^(?P<uuid>[\w-]+)/portfolio', views.profile_detail_portfolio, name='profile_detail_portfolio'),
    url(r'^(?P<uuid>[\w-]+)/', views.profile_detail, name='profile_detail'),
)
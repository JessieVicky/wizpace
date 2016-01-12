from django.conf.urls import patterns, url
from custom_projects import views

urlpatterns = patterns('',
    url(r'^add/search_skill/$', views.search_skill, name='projects_search_skill'),
    # url(r'^add/$', views.AddProject.as_view(), name='projects_add'),
    url(r'^add/$', views.add_project, name='projects_add'),
    url(r'^index/$', views.projects_index, name='projects_index'),
    url(r'^list/$', views.ListProjects.as_view(), name='projects_list')
)
from django.contrib import admin
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'wizpace.views.home', name='home'),
    url(r'^toc/$', 'wizpace.views.toc', name='toc'),
    url(r'^privacy/$', 'wizpace.views.privacy', name='privacy'),

    url(r'^profile/', include('user_profiles.urls')),
    url(r'^projects/', include('custom_projects.urls')),
    url(r'^account/', include('custom_reg.urls')),
    url(r'^account/', include('custom_settings.urls')),
    url(r'^account/', include('account.urls')),
)

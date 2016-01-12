from django.conf.urls import patterns, url
from custom_reg import views

urlpatterns = patterns('',
    url(r'^signup/', views.SignupView.as_view(), name='account_signup'),
    url(r'^login/', views.LoginView.as_view(), name='account_login'),
)
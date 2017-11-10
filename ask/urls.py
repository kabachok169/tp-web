"""web1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index, name='index'),

    url(r'^hot$', hot_questions, name='hot'),

    url(r'^tag/(?P<tag_name>[a-z A-Z 0-9]+)$', tag, name='tag'),

    url(r'^ask$', create_question, name='create_question'),

    url(r'^ask/save$', save_question, name='save_question'),

    url(r'^question/(?P<question_id>[0-9]+)$', one_question, name='question'),

    url(r'^settings$', settings, name='settings'),

    url(r'^login$', login, name='login'),
    url(r'^login/confirm$', login_confirm, name='auth'),
    url(r'^logout$', logout, name='logout'),

    url(r'^signup$', registrate, name='signup'),
    url(r'^signup/confirm$', registration_confirm, name='registrate'),

]



from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http.response import FileResponse, HttpResponseNotModified
from django.utils.http import http_date
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

import os


# def index(request):
#     return render(request, 'index.html')

class AboutView(TemplateView):
    template_name = 'index.html'

def data(request):

    pars = ''
    type = ''
    if len(request.POST):
        type = 'POST'
        for key in request.POST.keys():
            pars += key + '=' + request.POST[key]
            pars += '\n'


    if len(request.GET):
        type = 'GET'
        for key in request.GET.keys():
            pars += key + '=' + request.GET[key]
            pars += '<br>'



    context = {'type' : type,
                'params' : pars}

    return render(request, 'dz2.html', context)
    # return HttpResponse(os.listdir('./'))

def create_question(request):
    return render(request, 'ask.html')

def one_question(request):
    return render(request, 'question.html')

def settings(request):
    return render(request, 'settings.html')

def login(request):
    return render(request, 'login.html')

def registrate(request):
    return render(request, 'registration.html')

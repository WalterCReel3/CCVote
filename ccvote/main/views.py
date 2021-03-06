import logging
import datetime
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import GroupData
from main.models import UserData

#
# Example view demonstrating template rendering and data access
#
def home(request):
    page_data = {}
    page_data['project_name'] = 'City Council Voting'
    page_data['datetime'] = datetime.datetime.now()
    page_data['groups'] = GroupData.objects.all()
    page_data['users'] = UserData.objects.all()
    return render_to_response('main/home.html', page_data,
                              RequestContext(request))


class LoginForm(forms.Form):
    user_name = forms.CharField(label='Login', max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


#
# Example view demonstrating form handling
#
def login(request):
    page_data = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # TODO: do login stuff
            logging.info('Login attempt: %s:%s' % 
                         (form.cleaned_data['user_name'],
                          form.cleaned_data['password']))
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    page_data['form'] = form
    return render_to_response('main/login.html', page_data,
                               RequestContext(request))

# vim: set sts=4 sw=4 expandtab:

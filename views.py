from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .creds import env_file, google_service_account
from .silliness import random_hackers_quote

def wordpress_login(request):
    if request.method == "POST":
        if 'redirect_to' in request.POST:
            return HttpResponseRedirect(request.POST['redirect_to'])
    return render(request, 'skidaddle/login.html', context={})

def wordpress_troll(request):
    if 'HTTP_REFERER' in request.META:
        return render(request, 'skidaddle/image.html', context={'quote': random_hackers_quote()})
    return HttpResponseRedirect(reverse('skidaddle_wordpress_login'))

def dot_env(request, *args, **kwargs):
    return HttpResponse(env_file('txt'), content_type='text/plain')

def settings_json(request, *args, **kwargs):
    return HttpResponse(env_file('json'), content_type='application/json')

def google_service_json(request, *args, **kwargs):
    return HttpResponse(google_service_account(), content_type='application/json')

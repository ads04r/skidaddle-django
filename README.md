# Skidaddle: Django Version

A Django re-write of [my previous PHP project](https://github.com/ads04r/skidaddle). This is
a pluggable app you can add to your Django project that responds to scans for accidentally
exposed secrets files with realistic fake information and occasional snarky insults.

## Why?

Because when you waste the time of bad people, they're not spending that time harming
others. Also, it's funny.

## Installation

Clone into your project directory.   
Add `path('', include('skidaddle.urls')),` to the `urlpatterns` list in your main urls.py file.   
Ensure `'skidaddle',` is added to the `INSTALLED_APPS` list in `settings.py`.   
Run `python manage.py collectstatic` as appropriate.   
Restart your web server.   

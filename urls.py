from django.urls import re_path
from .views import dot_env, settings_json, google_service_json, wordpress_login, wordpress_troll

urlpatterns = [
    re_path(r'^wp-login.php$', wordpress_login, name='skidaddle_wordpress_login'),
    re_path(r'^wp-admin/$', wordpress_troll, name='skidaddle_wordpress_troll'),
	re_path(r'^(.*/)?\.env$', dot_env, name='skidaddle_dot_env'),
	re_path(r'^(.*/)?settings\.json$', settings_json, name='skidaddle_settings_json'),
	re_path(r'^(.*/)?service-account\.json$', google_service_json, name='skidaddle_google_service_json'),
]
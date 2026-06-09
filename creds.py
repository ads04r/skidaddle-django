from django.core.cache import cache
import random, string, json

def garbage_slug(length=8):
    cache_key = "random_slug_{}".format(length)
    ret = cache.get(cache_key) # We use caching to ensure the same 'password' is returned on multiple calls
    if not ret is None:
        return ret
    ret = ''.join(random.choices(string.ascii_lowercase, k=length))
    cache.set(cache_key, ret, 86400)
    return ret

def garbage_number(length=32):
    cache_key = "random_digits_{}".format(length)
    ret = cache.get(cache_key) # We use caching to ensure the same 'password' is returned on multiple calls
    if not ret is None:
        return ret
    ret = ''.join(random.choices(string.digits, k=length))
    cache.set(cache_key, ret, 86400)
    return ret

def garbage_hex_digest(length=40):
    cache_key = "random_hex_digest_{}".format(length)
    ret = cache.get(cache_key) # We use caching to ensure the same 'password' is returned on multiple calls
    if not ret is None:
        return ret
    ret = ''.join(random.choices(string.digits + 'abcdef', k=length))
    cache.set(cache_key, ret, 86400)
    return ret

def garbage_string(length=16):
    cache_key = "random_string_{}".format(length)
    ret = cache.get(cache_key) # We use caching to ensure the same 'password' is returned on multiple calls
    if not ret is None:
        return ret
    ret = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    cache.set(cache_key, ret, 86400)
    return ret

def garbage_pk():
    cache_key = "random_pk"
    ret = cache.get(cache_key) # We use caching to ensure the same 'password' is returned on multiple calls
    if not ret is None:
        return ret
    ret = '-----BEGIN PRIVATE KEY-----\n'
    for i in range(0, 35):
        ret = ret + ''.join(random.choices(string.ascii_letters + string.digits + '/+', k=70)) + '\n'
    ret = ret + ''.join(random.choices(string.ascii_letters + string.digits + '/+', k=34)) + '\n'
    ret = ret + '-----END PRIVATE KEY-----\n'
    cache.set(cache_key, ret, 86400)
    return ret

def env_file(format='json'):
    data = {
        "DB_HOST": "localhost",
        "DB_DATABASE": garbage_string(16),
        "DB_USERNAME": garbage_string(8),
        "DB_PASSWORD": garbage_string(24)
    }
    if format == 'txt':
        return '\n'.join(["{}={}".format(k, v) for k, v in data.items()])
    return json.dumps(data)

def google_service_account():
    project_id = "{}-{}".format(garbage_slug(6), garbage_string(5))
    key_id = garbage_hex_digest(40)
    return json.dumps({
        "type": "service_account",
        "project_id": project_id,
        "private_key_id": garbage_hex_digest(),
        "private_key": garbage_pk(),
        "client_email": "firebase-adminsdk-fbsvc@{}.iam.gserviceaccount.com".format(project_id),
        "client_id": garbage_number(21),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40{}.iam.gserviceaccount.com".format(project_id),
        "universe_domain": "googleapis.com"
    })

https://docs.djangoproject.com/zh-hans/2.1/

python manage.py test polls

Django 中间件:

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

process_request(request)
process_view(request, callback, callback_args, callback_kwargs)
process_template_response(request, response)
process_exception(request, exception)
process_response(request, response)


# 比如统计一分钟访问页面数，太多就把他的 IP 加入到黑名单 BLOCKED_IPS
class BlockIpMiddleware(object):
    def process_request(self, request):
        if request.META['REMOTE_ADDR'] in getattr(settings, 'BLOCKED_IPS', []):
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')


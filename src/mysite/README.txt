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


<!-- 新 Bootstrap4 核心 CSS 文件 -->
<!-- 如果只是想使用样式，不涉及交互等操作，可以不引入JS文件 -->
<link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.1.0/css/bootstrap.min.css">
 
<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
 
<!-- popper.min.js 用于弹窗、提示、下拉菜单 -->
<script src="https://cdn.bootcss.com/popper.js/1.12.5/umd/popper.min.js"></script>
 
<!-- 最新的 Bootstrap4 核心 JavaScript 文件 -->
<script src="https://cdn.bootcss.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>


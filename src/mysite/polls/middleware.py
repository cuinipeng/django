from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class M1(MiddlewareMixin):
    def process_request(self, request):
        print('M1.process_request')
        # 如果此处有 return, 后面的不执行, 直接返回给用户
        return HttpResponse('M1.DirectResponse')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('M1.process_view')

    def process_template_response(self, request, response):
        print('M1.process_template_response')
        return response

    def process_response(self, request, response):
        print('M1.process_response')
        return response

    def process_exception(self, request, exception):
        print('M1.process_exception')


class M2(MiddlewareMixin):
    def process_request(self, request):
        print('M2.process_request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('M2.process_view')

    def process_template_response(self, request, response):
        print('M2.process_template_response')
        return response

    def process_response(self, request, response):
        print('M2.process_response')
        return response

    def process_exception(self, request, exception):
        print('M2.process_exception')

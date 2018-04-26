# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/26'
import http


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    input = environ['PATH_INFO'][1:] or 'web'
    print(input)
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

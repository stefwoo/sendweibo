#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, post, request
from initclient import initclient
import weibo

APP_KEY = '1021805059' # app key
APP_SECRET = 'fc6af22b6147925b79c08ad5adfee78c' # app secret
CALL_BACK = 'https://api.weibo.com/oauth2/default.html' # callback url

from bottle import static_file
@route('/<filename>')
def send_image(filename):
    print filename
    return static_file(filename, root='')

@route('/')
def hello():
    client = initclient.myAPIClient(APP_KEY, APP_SECRET, CALL_BACK)
    auth_url = client.get_authorize_url()
    print auth_url
    return '''<head><link rel="stylesheet" type="text/css" href="http://localhost:8080/tg.css" /></head>
            <p>这是一个应用方便监控具体的某个关注者的微博更新情况，需要认证，<a href=%s>认证</a></p>'''%auth_url

@route('/code=<code>')
def auth(code):
    print type(code)
    #return "<>"
    return '''OK了，已经认证帐号了，请给出你要监控的关注者的id（目前只支持监控一个id，改进中，谢谢）。
                <form method="POST" action="/login">
                    <input name="name"     type="text" />
                    <input type="submit" />
                </form>'''


@post('/login') # or @route('/login', method='POST')
def login_submit():
    uid = request.forms.get('name')
    print uid
    print type(uid)
    return "程序已经开始自动运行，如有新信息会已邮件通知你的。你关注的用户是：%s"%uid



@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


run(host='localhost', port=8080, debug=True)#, reloader=True)

# -*- coding: utf-8 -*-
import requests
from html.parser import HTMLParser


class DoubanClient(object):
    def __init__(self):
        object.__init__(self)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                   'origin': 'http://www.douban.com'}
        self.session = requests.session()
        self.session.headers.update(headers)


    def login(self, number):
        data = {'area_code': '+86',
                'ck': '',
                'number': number}
        headers = {'referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
                   'Origin': 'https://accounts.douban.com'}
        url = 'https://accounts.douban.com/j/mobile/login/request_phone_code'
        # r = self.session.get(url)
        self.session.post(url, data=data, headers=headers)
        # (captcha_id, captcha_url) = _get_captcha(r.content)
        code = input("Please input phone code: ")
        url = 'https://accounts.douban.com/j/mobile/login/verify_phone_code'
        data = {'area_code': '+86',
                'ck': '',
                'number': number,
                'code': code,
                'ticket': '',
                'remember': 'false'}
        headers = {'referer': 'https://accounts.douban.com/passport/login',
                   'Origin': 'https://accounts.douban.com'}
        r = self.session.post(url, data=data, headers=headers)
        print(r.content)
        print(self.session.cookies.items())

    def edit_signature(self, username, signature):
        url = 'https://www.douban.com/people/%s/' % username
        r = self.session.get(url)
        data = {'ck': _get_ck(r.content), 'signature': signature}
        url = 'https://www.douban.com/j/people/%s/edit_signature' % username
        headers = {'referer': url,
                   'host': 'www.douban.com',
                   'x-requested-with': 'XMLHttpRequest'}
        r = self.session.post(url, data=data, headers=headers)
        print(r.content)


def _attr(attrs, attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None


def _get_captcha(content):

    class CaptchaParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.captcha_id = None
            self.captcha_url = None

        def handle_starttag(self, tag, attrs):
            if tag == 'img' and _attr(attrs, 'id') == 'captcha_image' and _attr(attrs, 'class') == 'captcha_image':
                self.captcha_url = _attr(attrs, 'src')

            if tag == 'input' and _attr(attrs, 'type') == 'hidden' and _attr(attrs, 'name') == 'captcha-id':
                self.captcha_id = _attr(attrs, 'value')

    p = CaptchaParser()
    p.feed(content)
    return p.captcha_id, p.captcha_url


def _get_ck(content):

    class CKParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.ck = None

        def handle_starttag(self, tag, attrs):
            if tag == 'input' and _attr(attrs, 'type') == 'hidden' and _attr(attrs, 'name') == 'ck':
                self.ck = _attr(attrs, 'value')

    p = CKParser()
    p.feed(content)
    return p.ck


if __name__ == '__main__':
    c = DoubanClient()
    c.login('18902212023')
    # c.edit_signature('username', 'python 爬虫基础')

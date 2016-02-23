# -*- coding: utf-8 -*-
import urllib.request as request
from html.entities import name2codepoint
from html.parser import HTMLParser


class BashImRequest(request.Request):
    def __init__(self, url=None, *args, **kwargs):
        self.url = url or 'http://bash.im/'
        super(BashImRequest, self).__init__(self.url, *args, **kwargs)
        self.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0')
        self.page = ''

    def get_page(self):
        self.page = request.urlopen(self).read().decode('windows-1251')
        return self.page


class BashImParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        super(BashImParser, self).__init__(*args, **kwargs)
        self.key_data = False
        self.key_id = False
        self.data = ''
        self.number = None
        self.results = []

    def handle_starttag(self, tag, attrs):
        if self.key_data and tag == 'br':
            self.data += '<br>'
        for attr in attrs:
            if attr[1] == 'text' and attr[0] == 'class':
                self.key_data = True
            if attr[1] == 'id' and attr[0] == 'class':
                self.key_id = True

    def handle_data(self, data):
        if self.key_data:
            self.data += data
        if self.key_id:
            self.number = int(data[1:])

    def handle_entityref(self, name):
        if self.key_data:
            data = chr(name2codepoint[name])
            self.data += data

    def handle_charref(self, name):
        if self.key_data:
            if name.startswith('x'):
                data = chr(int(name[1:], 16))
            else:
                data = chr(int(name))
            self.data += data

    def handle_endtag(self, tag):
        if self.key_data:
            self.results.append((self.number, self.data))
            self.data = ''
            self.number = None

        self.key_data = False
        self.key_id = False

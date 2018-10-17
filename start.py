# -*- encoding:utf-8 -*-
from bottle import run
from web_engine import *

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
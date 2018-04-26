# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/26'

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


if __name__ == '__main__':
    app.run()


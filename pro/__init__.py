#-*- coding:utf-8 -*-
#============================================================
#作者：韩望
#日期：2017-04-02
#功能：初始化函数
#默认函数更新：无
#备注：无
#============================================================
from flask import Flask

#-----------create app----------
app = Flask(__name__)
app.config.from_object("frame.config")
app.config['SECRET_KEY'] = '123456'

from view import default,users

#-*- coding:utf-8 -*-
#============================================================
#作者：韩望
#日期：2017-04-02
#功能：默认视图函数
#默认函数更新：无
#备注：无
#============================================================
from flask import Flask,session,url_for
from flask import render_template,request,redirect
from pro import app
from pro.model.admin  import Admin
from pro.model.conference import Conference
from pro.model.storepicture import StorePicture
from pro.model.users import Users
import json,sys
from frame import const
reload(sys)
sys.setdefaultencoding('utf-8')

#用户信息查询
@app.route("/admin/<id>/info")
def admininfo(id):
    try:
        str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","Adminid","AdminName","AdminPhone","AdminEmail","AdminCsrq"))
        tuple_result = Admin.select(cols=str_col,where=("usersid=%s" % (id)))
        return render_template("admin_list.html",**locals())
    except:
        return redirect(url_for("userlist"))

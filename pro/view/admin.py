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
@app.route("/admin/list")
def admin_list():
    try:
        str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","Adminid","AdminName","AdminPhone","AdminEmail","AdminCsrq"))
        tuple_result = Admin.select(cols=str_col)
        return render_template("admin_list.html",**locals())
    except:
        return redirect(url_for("userlist"))


#用户信息查询
@app.route("/admin/<id>/info")
def admin_info(id):
    try:
        str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","Adminid","AdminName","AdminPhone","AdminEmail","AdminCsrq"))
        tuple_result = Admin.select(cols=str_col,where=("usersid=%s" % (id)))
        return render_template("admin_list.html",**locals())
    except:
        return redirect(url_for("userlist"))

#管理员修改个人资料
@app.route("/admin/<id>/edit",methods=["POST","GET"])
def admin_info_edit(id):
    map_where={}
    if request.method == "POST":
        AdminName =request.form["adminName"]
        if len(AdminName) != 0:
            map_where["AdminName"] = AdminName
        AdminTrueName =request.form["adminTrueName"]
        if len(AdminTrueName) != 0:
            map_where["AdminTrueName"] = AdminTrueName
        AdminAddress =request.form["adminAddress"]
        if len(AdminAddress) != 0:
            map_where["AdminAddress"] = AdminAddress
        AdminEmail =request.form["adminEmail"]
        if len(AdminEmail) != 0:
            map_where["AdminEmail"] = AdminEmail
        AdminSpecialty =request.form["adminSpecialty"]
        if len(AdminSpecialty) != 0:
            map_where["AdminSpecialty"] = AdminSpecialty
        AdminHuji =request.form["adminHuji"]
        if len(AdminHuji) != 0:
            map_where["AdminHuji"] = AdminHuji
        AdminIDcard =request.form["adminIDcard"]
        if len(AdminIDcard) != 0:
            map_where["AdminIDcard"] = AdminIDcard
        AdminCsrq =request.form["adminCsrq"]
        if len(AdminCsrq) != 0:
            map_where["AdminCsrq"] = AdminCsrq
        AdminJiguan =request.form["adminJiguan"]
        if len(AdminJiguan) != 0:
            map_where["AdminJiguan"] = AdminJiguan
        AdminAge =request.form["adminAge"]
        if len(AdminAge) != 0:
            map_where["AdminAge"] = AdminAge
        AdminSex =request.form["adminSex"]
        if len(AdminSex) != 0:
            map_where["AdminSex"] = AdminSex
        AdminPhone =request.form["adminPhone"]
        if len(AdminPhone) != 0:
            map_where["AdminPhone"] = AdminPhone
        str_sql_where = (" ID = %s")
        print(map_where)
        print("str_sql=%s" % str_sql_where)
        Admin.update_dict(map_where,str_sql_where,[id])
        return redirect(url_for("admin_list"))
    str_col = ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % ("Adminid","AdminName","AdminTrueName","AdminAddress","AdminEmail","AdminSpecialty","AdminHuji","AdminIDcard","AdminCsrq","AdminJiguan","AdminAge","AdminSex","AdminPhone"))
    tuple_result = Admin.select(cols=str_col,where=(" ID = %s" % (id)))
    return render_template("admin_edit.html",**locals())

#管理员密码修改
@app.route("/admin/<id>/pwd",methods=["POST","GET"])
def admin_pwd_update(id):
    try:
        str_col = (" %s,%s " % ("AdminPass","AdminPassQuestion"))
        tuple_result = Admin.select(cols=str_col,where=("usersid=%s" % (id)))
        adminpass = tuple_result[0][0]
        adminpassquestion = tuple_result[0][1]
        if len(adminpassquestion) == 0:
            adminpassquestion = "没有密码保护问题"
        if request.method == "POST":
            map_where ={}
            str_adminpassreply = request.form["adminpassreply"].strip()
            map_where["AdminPassQuestion"] = str_adminpassreply
            str_adminrepass = request.form["adminrepass"].strip()
            str_adminpassnew = request.form["adminpassnew"].strip()
            map_where["AdminPass"] = str_adminpassnew
            str_adminrepassnew = request.form["adminrepassnew"].strip()
            map_where["AdminRepass"] = str_adminrepassnew
            if str_adminpassnew != str_adminrepassnew:
                return ("新密码与确认密码不一致")
            str_sql_where = (" ID = %s")
            if str_adminpassreply == adminpassquestion:
                if adminpass == str_adminrepass:
                    Admin.update_dict(map_where,str_sql_where,[id])
                    return redirect(url_for("admin_list"))
                else:
                    return ("输入原始密码不正确，请返回重新输入")
            else:
                return ("密码保护问题不正确，请返回重新输入")
        return render_template("admin_pwd_update.html")
    except:
        return render_template("admin_pwd_update.html")
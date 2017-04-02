#-*- coding:utf-8 -*-
#coding=utf-8
#============================================================
#作者：韩望
#日期：2017-04-02
#功能：数据库的二次封装
#更新：无
#备注：无
#============================================================
from flask import Flask,session,url_for
from flask import render_template,request
from pro import app
from pro.model.node_info  import NodeInfo
import json

@app.route('/',methods=['POST','GET'])
def show_default():
	current_id = 8
	if request.method=='POST':
		current_id = request.form['current_id',1]
	current_name = NodeInfo.select(cols='name',where=("id = %s"% current_id))[0]
	print("=====================start ========================")
	print (current_name)
	print str(json.dumps(current_name))
	session['default_name'] = json.dumps(current_name)
	print("=====================  end ========================")
	return render_template('default.html',**locals())

@app.route('/fangwuchuzu')
def fangwuchuzu():
	return render_template('sub1/fangwuchuzu.html')


@app.route('/selectaddr')
def selectaddr():
	return render_template('selectaddr.html')

@app.route('/test')
def test():
	return "hello world!"

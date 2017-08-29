# -*-coding=utf-8 -*-

from flask import render_template,request,url_for,redirect
from app import app
from getIp import getIp
from sic2nacis import sic2nacis
from extractString import extractStringMain

@app.route('/')
def index():
	return "welcome"


@app.route("/show")
def showTerminal():
	return render_template("terminal.html",ip=getIp())

@app.route("/show_extract")
def showTerminal_extract():
	return render_template("terminal_extract.html",ip=getIp())
	

@app.route('/reply',methods=['POST','GET'])
def reply():
	if request.method=='POST':
		youAsk=request.form['name']
		return render_template("reply.html",
		yourRequest=youAsk,
		result=sic2nacis(youAsk))

		
	else:
		youAsk=request.args.get("name")
		return "error while handling %s"%youAsk
		#return success(youAsk,getDataMysql(youAsk),"static/figure.png")
		#return redirect(url_for('success',someText=userName,result=getDataMysql()))

@app.route('/reply_extract',methods=['POST','GET'])
def reply_extract():
	if request.method=='POST':
		youAsk=request.form['name']
		return render_template("reply_extract.html",
		yourRequest=youAsk,
		result=extractStringMain(youAsk))

		
	else:
		youAsk=request.args.get("name")
		return "error while handling %s"%youAsk		
		
@app.route("/null")
def null():
	return render_template("/null.html",message="页面建设中")

from flask import Flask
from flask import render_template
from pro import app

@app.route('/')
def show_default():
	return render_template('default.html')

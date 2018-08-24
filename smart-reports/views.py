from flask import Flask, url_for, render_template
from app import app
from devoptions import *

#server/
@app.route('/')
def home(name=None):
    return render_template('index.html', \
                           name=name,\
                           calendarcodegen=get_js_maincalendar())
    

# cada uno de estos es una direccion aparte
# server/aboutus
@app.route('/aboutus')
def aboutus():
    return "<h2>about us</h2>"

#server/question/<title>
#con esto se puede pedir directamente una URL
# vanity URL
@app.route('/question/<title>')
def question(title):
    return '<h2>' + title + '</h2>'







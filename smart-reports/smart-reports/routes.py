from flask import Flask, url_for
from app import app


#server/
@app.route('/')
def hello():
    createLink= "<a href='" + url_for('aboutus') + "'>Create a question</a>";
    return """Hello World!""" + createLink
    

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

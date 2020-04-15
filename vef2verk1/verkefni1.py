import os
from flask import Flask, render_template, request, json
from datetime import datetime
import os
import urllib.request
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <p><a                                                                                                                                                                                                                                                                                                                                                                                     href="/sida2" title="Síða 2">Síða 2 </a> | <a href="/sida3" title="Síða 3">Síða 3 </a></p>
    <img src="http://loremflickr.com/600/400" />
    """

@app.route('/sida2')
def page2():
    return """
    <h1>Síða 2</h1>
    <p><a href="/" title="Forsíða">Forsíða </a> | <a href="/sida3" title="Síða 3">Síða 3 </a></p>
    <p>It is currently cathour.</p>
    <img src="http://loremflickr.com/600/400" />
    """ 
@app.route('/sida3')
def page3():
    return render_template('sida3.html')
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, use_reloader=True)
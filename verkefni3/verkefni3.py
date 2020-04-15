import os
from flask import Flask, flash, redirect, render_template, request, json
from datetime import datetime
from jinja2 import ext
import urllib.request
app = Flask(__name__)

with urllib.request.urlopen("https://apis.is/petrol/") as url:
    gogn = json.loads(url.read().decode())

def format_time(gogn):
    return datetime.strptime(gogn, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d. %m. %Y Klukkan: %H:%M')
app.jinja_env.filters['format_time'] = format_time
#{{ gogn.timestampPriceCheck | format_time }}
app.jinja_env.add_extension(ext.do)


def minPetrol():
    minPetrolPrice = 1000
    company = None
    address = None
    lst = gogn['results']
    for i in lst:
        if i['bensin95'] is not None:
            if i['bensin95'] < minPetrolPrice:
                minPetrolPrice = i['bensin95']
                company = i['company']
                address = i['name']
    return [minPetrolPrice, company, address]
def minDiesel():
    minDieselPrice = 1000
    company = None
    address = None
    lst = gogn['results']
    for i in lst:
        if i['diesel'] is not None:
            if i['diesel'] < minDieselPrice:
                minPetrolPrice = i['diesel']
                company = i['company']
                address = i['name']
    return [minDieselPrice, company, address]
@app.route('/')
def homepage():
    return render_template('index.html', gogn=gogn, minP=minPetrol(), minD=minDiesel())

@app.route('/company/<company>')
def comp(company):
    return render_template('company.html', gogn=gogn, com=company)

@app.route('/moreinfo/<key>')
def info(key):
    return render_template('moreinfo.html', gogn=gogn, k=key)

@app.errorhandler(404)
def pagnotfound(error):
    return render_template('pagenotfound.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
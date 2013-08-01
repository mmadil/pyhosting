# Imports

from bottle import route, run, static_file
from bottle import jinja2_template
from sys import argv
from jinja2 import Template


# Some settings necessary for deploying app to heroku
# and users that be using this project to upload their pages.

local = False
users = ['adil',]
STATIC_URL = 'https://googledrive.com/host/0B-gIhJMz12Bta21xOFVKc3ZWWEk/'

# Helper functions 

def Raise404():
    try:
        file = open('templates/404.html', 'rU')
        page = file.read()
        context = {'STATIC_URL': STATIC_URL,}
        page = jinja2_template(page, context)
        return page
    except IOError:
        print "Please create a 404.html"
        return "<h1>404 - Page not found </h1>"


def ReadPage(*args):
    if len(args) == 0:
        try:
            file = open('templates/index.html', 'rU')
            page = file.read()
            context = {'STATIC_URL': STATIC_URL, 'users': len(users),}
            page = jinja2_template(page, context)
            return page
        except IOError:
            return Raise404()

    if len(args) == 1:
        try:
            file = open('profiles/' + str(args[0]) + '/index.html', 'rU')
            page = file.read()
            return page
        except IOError:
            return Raise404()

    if len(args) == 2:
        try:
            file = open('profiles/' + str(args[0] + '/' + str(args[1])), 'rU')
            page = file.read()
            return page
        except IOError:
            return Raise404()



# Route for Main Home page.

@route('/')
def Homepage():
    return ReadPage()


# Route for Users Home page
# takes one argument - name

@route('/<name>')
def UserHomePage(name):
    if name in users:
        return ReadPage(name)
    else:
        return Raise404()



# Route for pages / files that has been added by
# a user. Takes two arguments - name, page

@route('/<name>/<page>')
def UserOtherPages(name, page):
    if name in users:
        return ReadPage(name, page)
    else:
        return Raise404()



# Usage is only when developing locally.
# local_settings.py has local = True

try:
    from local_settings import local
except ImportError:
    pass


# Heroku uses different settings

if local:
    run(host='127.0.0.1', port=8000, debug=True, reloader=True)
else:
    run(host='0.0.0.0', port=argv[1], debug=False, reloader=True)



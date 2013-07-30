# Imports

from bottle import route, run
from sys import argv


# Some settings necessary for deploying app to heroku
# and users that be using this project to upload their pages.

local = False
users = ['adil',]

# Helper functions 

def Raise404(*args):
    try:
        file = open('')
        pass
    except IOError:
        pass

# Route for Main Home page.

@route('/')
def Homepage():
    return "Welcome this is Home screen"



# Route for Users Home page
# takes one argument - name

@route('/<name>')
def UserHomePage(name):
    if name in users:
        try:
            file = open('profiles/'+ str(name)+'/index.html', 'rU')
            page = file.read()
            return page
        except IOError:
            return "404"
    else:
        return "404"



# Route for pages / files that has been added by
# a user. Takes two arguments - name, page

@route('/<name>/<page>')
def UserOtherPages(name, page):
    if name in users:
        try:
            file = open('profiles/' + str(name) + '/'+ str(page), 'rU')
            page = file.read()
            return page
        except IOError:
            return "404"
    else:
        return "404"



# Usage is only when developing locally.

try:
    from local_settings import local
except ImportError:
    pass

# Heroku uses different settings than the one developed
# locally

if local:
    run(host='127.0.0.1', port=8000, debug=True)
else:
    run(host='0.0.0.0', port=argv[1], debug=False)



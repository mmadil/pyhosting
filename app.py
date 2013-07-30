from bottle import route, run
from sys import argv

local = False

users = ['adil',]

@route('/')
def Homepage():
    return "Welcome this is Home screen"

@route('/<name>')
def UserPage(name):
    if name in users:
        return "Welcome %s" % name
    else:
        return "404"

try:
    from local_settings import local
except ImportError:
    pass


if local:
    run(host='127.0.0.1', port=8000, debug=True)
else:
    run(host='0.0.0.0', port=argv[1], debug=False)

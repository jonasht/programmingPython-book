#!/usr/bin/python

import cgi

form = cgi.FieldStorage()
print('content-type : text/html\n')
print('<title> Reply page</title>')
if not 'user' in form:
    print('<h1> quem eh voce?</h1>')
else:
    print('<h1>hello<i>!</h1>' % cgi.escape(form['user'].value))

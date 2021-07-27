import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.' # onde html files estao
port = 80


os.chdir(webdir)
srvraddr = ('', port)

srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
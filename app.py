from flask import Flask, jsonify
#from pyodata.v2.service import Service
from odata_generator import xml_string, r_forward_data
from flask import make_response, jsonify
import xml.etree.cElementTree as ET
from pyslet.odata2.server import Server
from wsgiref.simple_server import make_server
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from memcache.memcache import main
from werkzeug.exceptions import NotFound
app = Flask(__name__)
app_2 = main('http://localhost:8080/odata.svc/')
application = DispatcherMiddleware(NotFound, {
    '': app
})

# get from http://localhost:8080/Rates('25')?$format=json

@app.route('/', methods=['GET', 'POST'])
def home():
    return "home page"

def run_cache_server(cache_app):
    SERVICE_PORT = 8080
    SERVICE_ROOT = "http://localhost:%i/" % SERVICE_PORT
    """Starts the web server running"""
    server = make_server('localhost', port=8080, app=cache_app)
    # Respond to requests until process is killed
    server.serve_forever()

if __name__ == '__main__':
    #app.run(debug=True)
    run_cache_server(application)
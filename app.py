from flask import Flask
from wsgiref.simple_server import make_server
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from memcache.memcache import main

app = Flask(__name__)  # default flask application
app_2 = main('http://localhost:8080/odata.svc/')  # this one is the schema base, we may need to make it dynamic
application = DispatcherMiddleware(app, {
    '/odata.svc': app_2  # second wsgi application, it can be pyslet server
})


# get from http://localhost:8080/odata.svc/
# get from http://localhost:8080/odata.svc/Rates('1')?$format=json
# get from http://localhost:8080/odata.svc/Rates

# get from http://localhost:8080/Rates('25')?$format=json

@app.route('/', methods=['GET', 'POST'])
def home():
    return "Home page"


def run_cache_server(cache_app):
    SERVICE_PORT = 8080
    """Starts the web server running"""
    server = make_server('localhost', port=8080, app=cache_app)
    # Respond to requests until process is killed
    server.serve_forever()


if __name__ == '__main__':
    # app.run(debug=True)
    run_cache_server(application)

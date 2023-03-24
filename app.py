from flask import Flask, jsonify
#from pyodata.v2.service import Service
from odata_generator import xml_string, r_forward_data
from flask import make_response, jsonify
import xml.etree.cElementTree as ET

app = Flask(__name__)

@app.route('/odata')
def odata():
    #headers = dict(r_forward.headers)
    response = make_response(r_forward_data.text)
    headers = {}
    headers["Content-Type"] = "application/json; odata.metadata=minimal"
    headers["OData-Version"] = "4.0"
    headers["OData-MaxVersion"] = "4.0"
    # headers[] =
    # headers[] =
    # headers[] =
    # headers[] =
    for key, value in headers.items():
        response.headers[key] = value
    return response

@app.route('/meta')
def odata():
    #headers = dict(r_forward.headers)
    response = make_response(r_forward_data.text)
    headers = {}
    headers["Content-Type"] = "application/json; odata.metadata=minimal"
    headers["OData-Version"] = "4.0"
    headers["OData-MaxVersion"] = "4.0"
    # headers[] =
    # headers[] =
    # headers[] =
    # headers[] =
    for key, value in headers.items():
        response.headers[key] = value
    return response

if __name__ == '__main__':
    app.run(debug=True)
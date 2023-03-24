from flask import Flask, jsonify
import pyodata
import requests
import pyodata.v2.service
app = Flask(__name__)
SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'


@app.route('/odata/<entityset>')
def odata(entityset):
    HTTP_LIB = requests.Session()

    northwind = pyodata.Client(SERVICE_URL, HTTP_LIB)

    for customer in northwind.entity_sets.Customers.get_entities().execute():
        print(customer.CustomerID, customer.CompanyName)
    return jsonify({"value": "data"})

if __name__ == '__main__':
    app.run(debug=True)
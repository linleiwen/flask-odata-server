from flask import Flask, Response, request
from pyslet.odata2.server import ODataServer, ReadOnlyEntitySet
from pyslet.odata2.sqlds import SqlDataStore

app = Flask(__name__)

# create a data store and populate it with some data
store = SqlDataStore("sqlite:///mydata.db")
# create an entity set for the "employees" entity
employees = ReadOnlyEntitySet(store, "employees")
# add some sample data to the "employees" entity set
employees.new_entity(Name="John Smith", Age=30, Department="Sales")
employees.new_entity(Name="Jane Doe", Age=40, Department="Marketing")
employees.new_entity(Name="Bob Johnson", Age=50, Department="Finance")
store.commit()

# create an OData server with the "employees" entity set
server = ODataServer()
server.data_sources["mydata"] = store
server.create_entity_set("employees", employees)

# define a Flask route for accessing the OData service
@app.route('/odata/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def odata(path):
    request.environ["HTTP_X_FORWARDED_FOR"] = request.remote_addr
    request.environ["SERVER_NAME"] = request.host
    request.environ["SERVER_PORT"] = str(request.host.split(":")[-1])
    request.environ["SCRIPT_NAME"] = "/odata"
    response = Response()
    request.method = request.method.upper()
    request.app = server
    request.environ["REMOTE_ADDR"] = request.remote_addr
    server.process_request(request, response)
    return response

if __name__ == '__main__':
    app.run(debug=True)
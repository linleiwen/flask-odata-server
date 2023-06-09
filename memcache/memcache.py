#! /usr/bin/env python
"""Creates an OData in-memory cache of key value pairs"""
import logging
from wsgiref.simple_server import make_server
from pyslet import iso8601 as iso
from pyslet.odata2 import metadata as edmx
from pyslet.odata2.memds import InMemoryEntityContainer
from pyslet.odata2.server import Server
from lib.utils import read_csv_to_df, datetime_to_unix_time
from pathlib import Path

SERVICE_PORT = 8080
SERVICE_ROOT = "http://localhost:%i/" % SERVICE_PORT
CLEANUP_SLEEP = 10


cache_app = None       #: our Server instance


def load_metadata():
    """Loads the metadata file from the current directory."""
    doc = edmx.Document()
    path = Path(__file__).parent / "MemCacheSchema.xml"
    with open(path, 'rb') as f:
        doc.read(f)
    return doc


def load_data(mem_cache):
    path = Path(__file__).parent / "../mock_data/sample_libor.csv"
    df_data = read_csv_to_df(path)
    with mem_cache.open() as collection:
        for index, row in df_data.iterrows():
            e = collection.new_entity()
            e.set_key(str(index))
            e['Date'].set_from_value(
                iso.TimePoint.from_unix_time(datetime_to_unix_time(row['Date'])))
            e['Libor'].set_from_value(row['Libor'])
            collection.insert_entity(e)



def run_cache_server(cache_app):
    """Starts the web server running"""
    #server = make_server('', SERVICE_PORT, cache_app)
    server = make_server('localhost', 8080, cache_app)
    logging.info("Starting HTTP server on port %i..." % SERVICE_PORT)
    # Respond to requests until process is killed
    server.serve_forever()




def main(service_root):
    """Executed when we are launched"""
    doc = load_metadata()
    InMemoryEntityContainer(doc.root.DataServices['MemCacheSchema.MemCache'])
    server = Server(serviceRoot=service_root)
    server.set_model(doc)
    # The server is now ready to serve forever
    load_data(doc.root.DataServices['MemCacheSchema.MemCache.Rates'])
    return server


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    server = main(SERVICE_ROOT)
    run_cache_server(server)

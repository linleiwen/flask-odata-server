import xml.etree.ElementTree as ET
import pandas as pd
import requests
# create a sample Pandas dataframe
df = pd.DataFrame({'id': [1, 2, 3], 'name': ['John', 'Jane', 'Bob'], 'age': [20, 30, 25]})

# create the root element for the OData XML document
root = ET.Element('feed', xmlns='http://www.w3.org/2005/Atom')

# create the entry elements for each row in the Pandas dataframe
for i, row in df.iterrows():
    entry = ET.SubElement(root, 'entry')
    id = ET.SubElement(entry, 'id')
    id.text = str(row['id'])
    name = ET.SubElement(entry, 'name')
    name.text = row['name']
    age = ET.SubElement(entry, 'age')
    age.text = str(row['age'])

# create the XML string from the root element
xml_string = ET.tostring(root)

# print the XML string
print(xml_string)

r = requests.get("https://services.odata.org/V4/Northwind/Northwind.svc/Categories")
xml_string_http = r.text
r_forward_data = r

r = requests.get("https://services.odata.org/V4/Northwind/Northwind.svc/$metadata#Categories")
xml_string_http = r.text
r_forward_data = r

print(r)
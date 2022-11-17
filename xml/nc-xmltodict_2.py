### XML Parsing into json => easier than xml.etree
###!pip install xmltodict
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Starting  -- XMLTODICT')
import json
import xmltodict
import os
#### delete line from XML file: <?xml version="1.0" encoding="UTF-8"?>
print(os.getcwd())
xmlfile = open("myfile.xml")
doc = xmltodict.parse(xmlfile.read())
#print('----SHOW RAW DICT/JSON----')
#print('RAW - serialized - string')
#print(doc)
#print('----SHOW DICT/JSON----')
#print('Prettified')
print(json.dumps(doc, indent=4))
#### Converting to str, and to json
str_doc = json.dumps(doc, indent=4)
json_doc = json.loads(str_doc)
####
print('----SHOW DATA TYPES----')
print(type(doc))
print(type(str_doc))
print(type(json_doc))
print('----SHOW STRUCTURE----')
print(json_doc.keys())
print(json_doc["rpc"].keys())
print(json_doc["rpc"]["edit-config"].keys())
print(json_doc["rpc"]["edit-config"]["config"].keys())
print(json_doc["rpc"]["edit-config"]["config"]["int8.1"].keys())
print('----SHOW OPERATIONS----')
print(json_doc["rpc"]["@message-id"])
print(json_doc["rpc"]["edit-config"]["default-operation"])
print(json_doc["rpc"]["edit-config"]["test-option"])
print(json_doc["rpc"]["edit-config"]["config"]["int8.1"]["@nc:operation"])

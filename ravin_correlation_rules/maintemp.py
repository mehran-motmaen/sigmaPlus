import xml
import xmltodict
import doc
import xmltodict
from main2 import *

# Read the XML file
with open('doc//sample.xml', 'r') as xml_file:
    xml_content = xml_file.read()

# Convert XML to dictionary
rule_dict = xmltodict.parse(xml_content)

creat_yaml_files('sampl.yml', rule_dict)
creat_json_files('sampl.json', rule_dict)

print(rule_dict)
#.............................

# Sample JSON data representing the rule
with open('sampl.json//rule.json', 'r') as json_file:
    json_data = json_file.read()


# Convert JSON to Python dictionary
rule_dict = json.loads(json_data)

print(rule_dict)

# Convert the dictionary to XML
xml_content = xmltodict.unparse(rule_dict, pretty=True)

# Write the XML content to a file
with open('rules.xml', 'w') as xml_file:
    xml_file.write(xml_content)






import json
import xmltodict
import doc

# def convert_xml_to_json(xml_file_path, json_file_path):
#     # Read the XML file
#     with open(xml_file_path, 'r') as xml_file:
#         xml_content = xml_file.read()
#
#     # Convert XML to dictionary
#     rule_dict = xmltodict.parse(xml_content)
#
#     # Write the dictionary to a JSON file
#     with open(json_file_path, 'w') as json_file:
#         json.dump(rule_dict, json_file, indent=2)
#
# def convert_json_to_xml(json_file_path):
#     # Read the JSON file
#     with open(json_file_path, 'r') as json_file:
#         json_content = json.load(json_file)
#
#     # Convert the dictionary to XML
#     xml_content = xmltodict.unparse(json_content, pretty=True)
#
#     # Print the XML content
#     print(xml_content)
#
# # Example usage:
# xml_file_path = 'doc//sample.xml'
# json_file_path = 'output.json'
#
# # Convert XML to JSON and print JSON content
# convert_xml_to_json(xml_file_path, json_file_path)
# with open(json_file_path, 'r') as json_file:
#     print(json_file.read())
#
# # Convert JSON to XML and print XML content
# convert_json_to_xml(json_file_path)

with open('doc//sample.json', 'r') as json_file:
    json_content = json.load(json_file)

print(json_content)

for key in json_content:
    for key_ in json_content[key]:
        print(key_)
# Define the configuration as a string
import copy
import json
import xmltodict
import yaml

#open file
with open("zeek_default_cobalt_strike_certificate.yml", 'r') as file:
    config = file.read()


#load_yaml_file
def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data


# Replace 'your_file.yaml' with the actual path to your YAML file
yaml_file_path = "zeek_default_cobalt_strike_certificate.yml"
data_dict = load_yaml_file(yaml_file_path)

produced_rule = {
    "@kbid": "",
    "@id": "",
    "@owner": "",
    "@ver": "",
    "@enable": "",
    "@file_name": "",
    "filter_list": {},
    "action": {},
    "regulation": {},
    "description": {},
}

def set_description(produced_rule,data_dict):
    if "titl" in data_dict:
        produced_rule["description"]["title"] = data_dict["title"]
    if "id" in data_dict:
        produced_rule["description"]["id"] = data_dict["id"]
    if "references" in data_dict:
        produced_rule["description"]["references"] = data_dict["references"]
    if "author" in data_dict:
        produced_rule["description"]["author"] = data_dict["author"]
    if "date" in data_dict:
        produced_rule["description"]["date"] = data_dict["date"]
    if "modified" in data_dict:
        produced_rule["description"]["modified"] = data_dict["modified"]
    if "fields" in data_dict:
        produced_rule["description"]["fields"] = data_dict["fields"]
    if "falsepositives" in data_dict:
        produced_rule["description"]["falsepositives"] = data_dict["falsepositives"]
def produced_rule_attributes(produced_rule):
    counter = 120000
    produced_rule["@kbid"] = str(counter) + "_1"
    produced_rule["@id"] = counter
    produced_rule["@owner"] = "user" #user or system
    produced_rule["@ver"] = "1"
    produced_rule["@enable"] = "t"
    produced_rule["@file_name"] = ""
    produced_rule["filter_list"] = {}
    produced_rule["action"] = {}
    produced_rule["regulation"] = {}
#filter_list...

def add_additional_data_element(meaning, operator, text):
    additional_data_element = {}
    additional_data_element["@meaning"] = meaning
    additional_data_element["@operator"] = operator
    additional_data_element["#text"] = text
    return additional_data_element

def add_group_element(not_, additional_data):
    group_list_element = {}
    group_list_element["@not"] = "false"
    group_list_element["additional_data"] = additional_data
    return group_list_element

def filter_list(produced_rule):
    produced_rule["filter_list"]["filter"] = []
    temp_filtr = {}
    temp_filtr["@id"] = 1
    temp_filtr["@weight"] = "1"
    temp_filtr["@name"] = "__".join(data_dict["tags"])

    ## temp_filtr["source"]
    temp_filtr["source"] = {}
    temp_filtr["source"]["ip"] = {}
    temp_filtr["source"]["ip"]["@location"] = "ANY"
    temp_filtr["source"]["port"] = "0-65535"
    # temp_filtr["target"]
    temp_filtr["target"] = {}
    temp_filtr["target"]["ip"] = {}
    temp_filtr["target"]["ip"]["@location"] = "ANY"
    temp_filtr["target"]["port"] = "0-65535"

    # temp_filtr["event_list"]
    temp_filtr["event_list"] = {}
    temp_filtr["event_list"]["event"] = {}
    temp_filtr["event_list"]["event"]["@sensor_type"] = "372"  # system
    temp_filtr["event_list"]["event"]["@class_type"] = ""

    # if exist tag in ravin rule
    # temp_filtr["event_list"]["event"]["tag"] = []
    # temp_tag = {}
    # temp_tag["@meaning"] = "@meaning"
    # temp_tag["#text"] = "#text"
    # temp_filtr["event_list"]["event"]["tag"].append(temp_tag)

    #...

    temp_filtr["additional_data_list"] = {}
    temp_filtr["additional_data_list"]["group"] = []

    if "product" in data_dict["logsource"]:
        additional_data_list_1 = []
        meaning="product"
        operator="EQ"
        text=data_dict["logsource"]["product"]
        additional_data_list_1.append(add_additional_data_element(meaning=meaning, operator=operator, text=text))
        group_element_01 = add_group_element(not_="false", additional_data=additional_data_list_1)
        temp_filtr["additional_data_list"]["group"].append(group_element_01)

    if "service" in data_dict["logsource"]:
        additional_data_list_2 = []
        meaning = "service"
        operator = "EQ"
        text = data_dict["logsource"]["service"]
        additional_data_list_2.append(add_additional_data_element(meaning=meaning, operator=operator, text=text))
        group_element_02 = add_group_element(not_="false", additional_data=additional_data_list_2)
        temp_filtr["additional_data_list"]["group"].append(group_element_02)

    #detection

    detection=copy.deepcopy(data_dict["detection"])
    print(detection)


    conditioin_dictionary={}
    for sel in detection:
        print(sel)
        if sel == "condition":
            pass
        else:
            additional_data_list = []

            conditioin_dictionary[sel]=additional_data_list
            for selection_element in detection[sel] :
                meaning = selection_element
                operator = "EQ"
                print(detection[sel] [selection_element])
                if isinstance(detection[sel][selection_element], str):
                    text = detection[sel][selection_element]
                    additional_data_list.append(add_additional_data_element(meaning=meaning, operator=operator, text=text))
                    group_element_02 = add_group_element(not_="false", additional_data=additional_data_list)
                    temp_filtr["additional_data_list"]["group"].append(group_element_02)

                else:
                    for value in detection[sel][selection_element] :
                        text = value
                        additional_data_list.append(add_additional_data_element(meaning=meaning, operator=operator, text=text))
                        group_element_02 = add_group_element(not_="false", additional_data=additional_data_list)
                        temp_filtr["additional_data_list"]["group"].append(group_element_02)

    print()

    # additional_data_list_1 = []
    # additional_data_list_1.append(add_additional_data_element(meaning="certificate", operator="EQ", text="8BB00EE"))
    # additional_data_list_1.append(add_additional_data_element(meaning="Service", operator="EQ", text="x509"))
    #
    # additional_data_list_2 = []
    # additional_data_list_2.append(add_additional_data_element(meaning="mechanism", operator="NEQ", text="dfgdfg"))
    #
    # group_element_01 = add_group_element(not_="false", additional_data=additional_data_list_1)
    # group_element_02 = add_group_element(not_="false", additional_data=additional_data_list_2)
    #
    # group = []
    # group.append(group_element_01)
    # group.append(group_element_02)
    #
    # temp_filtr["additional_data_list"]["group"]=group
    produced_rule["filter_list"]["filter"].append(temp_filtr)


def action(produced_rule):
    produced_rule["action"] = {}
    # rule["action"]["alert"]=
    produced_rule["action"]["alert"] = {}
    produced_rule["action"]["alert"]["@priority"] = data_dict["level"]
    produced_rule["action"]["alert"]["@category"] = data_dict["title"]  # Related to Raven
    produced_rule["action"]["alert"]["message"] = data_dict["description"]
    produced_rule["action"]["alert"]["source"] = {}
    produced_rule["action"]["alert"]["source"]["ip"] = {}
    produced_rule["action"]["alert"]["source"]["ip"]["@reference_type"] = "source"
    produced_rule["action"]["alert"]["source"]["ip"]["@reference_id"] = "1"
    produced_rule["action"]["alert"]["target"] = {}
    produced_rule["action"]["alert"]["target"]["ip"] = {}
    produced_rule["action"]["alert"]["target"]["ip"]["@reference_type"] = "target"
    produced_rule["action"]["alert"]["target"]["ip"]["@reference_id"] = "1"

    produced_rule["action"]["prerequisite"] = {}
    produced_rule["action"]["prerequisite"]["predicate"] = []
    predicate_element = {}
    predicate_element["@type"] = "Hopping"
    predicate_element["param"] = [{"@reference_type": "source.ip"}]
    produced_rule["action"]["prerequisite"]["predicate"].append(predicate_element)

    produced_rule["action"]["consequence"] = {}
    produced_rule["action"]["consequence"]["predicate"] = []
    consequence_element = {}
    consequence_element["@type"] = "Hopping"
    consequence_element["param"] = [{"@reference_type": "source.ip"}]
    produced_rule["action"]["consequence"]["predicate"].append(consequence_element)

def regulation(produced_rule):
    filter_temp = {}
    filter_temp["@id"] = 1
    produced_rule["regulation"]["sequence"] = {}
    produced_rule["regulation"]["sequence"]["filter"] = []
    produced_rule["regulation"]["sequence"]["filter"].append(filter_temp)



def main():
    set_description(produced_rule,data_dict)
    produced_rule_attributes(produced_rule)
    filter_list(produced_rule)
    action(produced_rule)
    regulation(produced_rule)

    # root xml
    main_rule = {}
    main_rule["rule"] = produced_rule

    # Convert dictionary to JSON string
    json_rule = json.dumps(main_rule, indent=4)
    dict_rule = json.loads(json_rule)

    # convrt dict to xml
    xml_data = xmltodict.unparse(dict_rule, pretty=True)

    # write xml file
    with open("produced_rule01.xml", "w") as file:
        file.write(xml_data)

main()
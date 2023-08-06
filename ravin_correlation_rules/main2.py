# appframework_django_exceptions.yml
import json
import os
import yaml
import sigma_payam as sp
import shutil

path_to_rules_ = ["rules", "rules-emerging-threats", "rules-placeholder", "rules-threat-hunting", "rules-compliance"]
path_to_rules = []
for path_ in path_to_rules_:
    path_to_rules.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), path_))

path_to_rules_this_dir = []
for path in path_to_rules:
    new_path = ''.join(path.split('new_app\\'))
    path_to_rules_this_dir.append(new_path)


def yield_next_rule_file_path(path_to_rules: list) -> str:
    for path_ in path_to_rules:
        for root, _, files in os.walk(path_):
            for file in files:
                if file.endswith('.yml'):
                    yield os.path.join(root, file)


def read_yaml_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf8") as file:
            yaml_data = yaml.safe_load(file)
            return yaml_data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except yaml.YAMLError as e:
        print(f"Error while parsing the YAML file: {e}")
    return None


def add_to_dict_with_list(dictionary, key, value):
    if key in dictionary:
        if not isinstance(dictionary[key], list):
            dictionary[key] = [dictionary[key]]
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]


def remove_duplicates_in_list(dictionary):
    for key in dictionary:
        def remove_duplicates_recursive(data):
            if isinstance(data, list):
                unique_list = []
                for item in data:
                    if item not in unique_list:
                        unique_list.append(item)
                return unique_list
            elif isinstance(data, dict):
                for k, v in data.items():
                    data[k] = remove_duplicates_recursive(v)
                return data
            else:
                return data

        if key in dictionary:
            dictionary[key] = remove_duplicates_recursive(dictionary[key])

def extract_attribute(dic, path):
    for file_path in yield_next_rule_file_path(path):
        yaml_data_as_dict = read_yaml_file(file_path)
        for key in yaml_data_as_dict:
            add_to_dict_with_list(dic, key, yaml_data_as_dict[key])


def create_dir(file_name):
    try:
        os.makedirs(file_name)
    except FileExistsError:
        shutil.rmtree(file_name)
        os.makedirs(file_name)


def creat_json_files(file_name, dic):
    create_dir(file_name)
    for key in dic:
        with open(f'{file_name}/{key}.json', 'w') as file:
            file.write(json.dumps(dic[key]))


def creat_yaml_files(file_name, dic):
    create_dir(file_name)
    for key in dic:
        with open(f'{file_name}/{key}.yml', 'w') as file:
            yaml.dump(dic[key], file)

def creat_xml_files(file_name, dic):
    create_dir(file_name)
    for key in dic:
        with open(f'{file_name}/{key}.xml', 'w') as file:
            file.write(dic[key], file)


def main():
    # extract_attribute(sp.main_dictionary, path_to_rules_this_dir)
    #
    # creat_json_files('json_files', sp.main_dictionary)
    # creat_yaml_files('yaml_files', sp.main_dictionary)
    #
    # remove_duplicates_in_list(sp.main_dictionary)
    #
    # creat_json_files('unique_json_files', sp.main_dictionary)
    # creat_yaml_files('unique_yaml_files', sp.main_dictionary)

    creat_json_files('unique_json_files', sp.main_dictionary)



main()

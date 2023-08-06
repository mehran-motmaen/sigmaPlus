# appframework_django_exceptions.yml
import json
import os
import yaml
import sigma_payam as sp

path_to_rules_ = ["rules", "rules-emerging-threats", "rules-placeholder", "rules-threat-hunting", "rules-compliance"]
path_to_rules = []
for path_ in path_to_rules_:
    path_to_rules.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), path_))
    # Helper functions

path_to_rules_this_dir = []

for path in path_to_rules:
    new_path = ''.join(path.split('new_app\\'))
    path_to_rules_this_dir.append(new_path)


# print(path_to_rules_this_dir)


def yield_next_rule_file_path(path_to_rules: list) -> str:
    for path_ in path_to_rules:
        for root, _, files in os.walk(path_):
            for file in files:
                if file.endswith('.yml'):
                    yield os.path.join(root, file)


# Loop to print all file paths
# for file_path in yield_next_rule_file_path(path_to_rules_this_dir):
#     print(file_path)


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


def remove_duplicates_in_list(dictionary, key):
    # if key in dictionary and isinstance(dictionary[key], list):
    #     # print(key)
    #     # print(dictionary[key])
    #     set(dictionary[key])
    #     dictionary[key] = list(set(dictionary[key]))
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
    counter = 0
    for file_path in yield_next_rule_file_path(path):
        yaml_data_as_dict = read_yaml_file(file_path)
        # print(yaml_data_as_dict)
        for key in yaml_data_as_dict:
            add_to_dict_with_list(dic, key, yaml_data_as_dict[key])
            # dic[key] = yaml_data_as_dict[key]


extract_attribute(sp.main_dictionary, path_to_rules_this_dir)

remove_duplicates_in_list(sp.main_dictionary, 'tags')


for key in sp.main_dictionary:
    print(key)
    with open(f'json_files/{key}.json', 'w') as file:
        file.write(json.dumps(sp.main_dictionary[key]))
    with open(f'yaml_files/{key}.yml', 'w') as file:
        yaml.dump(sp.main_dictionary[key], file)


print()

# print(sp.main_dictionary)

# Example usage:
# yaml_file_path = "appframework_django_exceptions.yml"
# yaml_data_as_dict = read_yaml_file(yaml_file_path)
# print(yaml_data_as_dict)

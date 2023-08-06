# def add_to_dict_with_list(dictionary, key, value):
#     """
#     Add a value to the dictionary as a list under the specified key.
#
#     Parameters:
#         dictionary (dict): The dictionary to which the value will be added.
#         key (hashable): The key for the entry.
#         value: The value to be appended to the list.
#
#     If the key doesn't exist in the dictionary, a new list will be created for the key.
#     If the key exists and its value is not a list, the value will be converted to a list.
#     """
#     if key in dictionary:
#         if not isinstance(dictionary[key], list):
#             dictionary[key] = [dictionary[key]]
#         dictionary[key].append(value)
#     else:
#         dictionary[key] = [value]
#
# def remove_duplicates_in_list(dictionary, key):
#     """
#     Remove duplicate values from the list stored under the specified key.
#
#     Parameters:
#         dictionary (dict): The dictionary from which the list will be modified.
#         key (hashable): The key for the entry containing the list.
#
#     If the key doesn't exist in the dictionary or the value is not a list, the function does nothing.
#     """
#     if key in dictionary and isinstance(dictionary[key], list):
#         dictionary[key] = list(set(dictionary[key]))
#
# # Example usage:
# my_dict = {}
# add_to_dict_with_list(my_dict, 'name', 'John')
# add_to_dict_with_list(my_dict, 'age', 30)
# add_to_dict_with_list(my_dict, 'hobbies', 'reading')
# add_to_dict_with_list(my_dict, 'hobbies', 'cooking')
#
# print("Original dictionary:", my_dict)
#
# remove_duplicates_in_list(my_dict, 'hobbies')
#
# print("Dictionary after removing duplicates:", my_dict)
import json

import yaml


def json_to_yaml(json_data):
    """
    Convert JSON data to YAML format.

    Parameters:
        json_data (str): JSON data as a string.

    Returns:
        str: The JSON data converted to YAML format.
    """
    try:
        data_dict = json.loads(json_data)
        yaml_data = yaml.dump(data_dict)
        return yaml_data
    except Exception as e:
        print(f"Error occurred while converting JSON to YAML: {e}")
        return None

# Example usage:
json_data = '{"name": "John", "age": 30, "hobbies": ["reading", "cooking"]}'
yaml_data = json_to_yaml(json_data)

if yaml_data:
    print(yaml_data)
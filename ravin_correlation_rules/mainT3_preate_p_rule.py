# def custom_map_function(key):
#     # Your custom mapping logic goes here
#     # For this example, we'll assume the value is the key itself in uppercase.
#     return key.upper()
#
# def fill_dictionary_with_map(input_dict, map_function):
#     for top_level_key in input_dict:
#         if isinstance(input_dict[top_level_key], dict):
#             for second_level_key in input_dict[top_level_key]:
#                 if isinstance(input_dict[top_level_key][second_level_key], dict):
#                     for third_level_key in input_dict[top_level_key][second_level_key]:
#                         input_dict[top_level_key][second_level_key][third_level_key] = map_function(third_level_key)
#                 else:
#                     input_dict[top_level_key][second_level_key] = map_function(second_level_key)
#         else:
#             input_dict[top_level_key] = map_function(top_level_key)
#     return input_dict
#
# p_r_dictionary2 = {
#   "rule": {
#     "@id": "",
#     "@owner": "",
#     "@kbid": "",
#     "@enable": "",
#     "@ver": "",
#     "@file_name": "",
#     "filter_list": { },
#     "action": {},
#     "regulation": {}
#   }
# }
#
# completed_dictionary = fill_dictionary_with_map(p_r_dictionary2, custom_map_function)
# print(completed_dictionary)
#

def custom_map_function(key):
    # Custom mapping logic
    if key.startswith("@"):
        return "YOUR_VALUE_HERE"
    elif "_type" in key:
        return "TYPE"
    elif "_id" in key:
        return "ID"
    elif "_name" in key:
        return "NAME"
    elif "_location" in key:
        return "LOCATION"
    elif "_reference_id" in key:
        return "REFERENCE_ID"
    elif "_reference_type" in key:
        return "REFERENCE_TYPE"
    else:
        return key.upper()

def fill_dictionary_with_map(input_dict, map_function):
    for top_level_key in input_dict:
        if isinstance(input_dict[top_level_key], dict):
            for second_level_key in input_dict[top_level_key]:
                if isinstance(input_dict[top_level_key][second_level_key], dict):
                    for third_level_key in input_dict[top_level_key][second_level_key]:
                        input_dict[top_level_key][second_level_key][third_level_key] = map_function(third_level_key)
                else:
                    input_dict[top_level_key][second_level_key] = map_function(second_level_key)
        else:
            input_dict[top_level_key] = map_function(top_level_key)
    return input_dict

p_r_dictionary2 = {
    "rule": {
        "@id": "",
        "@owner": "",
        "@kbid": "",
        "@enable": "",
        "@ver": "",
        "@file_name": "",
        "filter_list": {},
        "action": {},
        "regulation": {}
    }
}

completed_dictionary = fill_dictionary_with_map(p_r_dictionary2, custom_map_function)
print(completed_dictionary)


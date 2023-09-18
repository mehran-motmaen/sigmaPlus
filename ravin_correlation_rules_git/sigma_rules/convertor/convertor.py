# import json
# import os
# import shutil
# import dicttoxml
# import yaml
# import sigma_rules_yaml
# import maps
#
#
# def extract_sigma_rules():
#     path_to_rules_ = ["rules", "rules-emerging-threats", "rules-placeholder", "rules-threat-hunting",
#                       "rules-compliance"]
#     path_to_rules = []
#     for path_ in path_to_rules_:
#         path_to_rules.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), path_))
#
#     path_to_rules_this_dir = []
#     current_dir_path = 'ravin_correlation_rules_git\\convertor\\'
#     for path in path_to_rules:
#         new_path = ''.join(path.split(current_dir_path))
#         path_to_rules_this_dir.append(new_path)
#
#     def yield_next_rule_file_path(path_to_rules: list) -> str:
#         for path_ in path_to_rules:
#             for root, _, files in os.walk(path_):
#                 for file in files:
#                     if file.endswith('.yml'):
#                         yield os.path.join(root, file)
#
#     for file_path in yield_next_rule_file_path(path_to_rules_this_dir):
#         shutil.copy(file_path, 'sigma_rules_yaml')
#
#
# def convert_yaml_to_json():
#     dir_name = 'sigma_rules_yaml'
#     for filename in os.listdir('sigma_rules_yaml'):
#         if filename.endswith('.yml'):
#             path = os.path.join(os.path.dirname(os.path.realpath(__file__)), f'{dir_name}\\{filename}')
#             yaml_file_path = path
#             json_file_path = path.replace('.yml', '.json').replace('_yaml', '_json')
#
#             with open(yaml_file_path, 'r', encoding='utf-8') as yaml_file:
#                 yaml_data = yaml.safe_load(yaml_file)
#
#             with open(json_file_path, 'w') as json_file:
#                 json.dump(yaml_data, json_file, indent=4)
#
#
# def convert_json_to_xml():
#     dir_name = 'sigma_rules_json'
#     for filename in os.listdir('sigma_rules_json'):
#         if filename.endswith('.json'):
#             path = os.path.join(os.path.dirname(os.path.realpath(__file__)), f'{dir_name}\\{filename}')
#             json_file_path = path
#             xml_file_path = path.replace('.json', '.xml').replace('_json', '_xml')
#
#             # Load JSON data from a file
#             with open(json_file_path, 'r') as json_file:
#                 json_data = json.load(json_file)
#
#             # Convert JSON data to XML
#             xml_data = dicttoxml.dicttoxml(json_data)
#
#             # Save XML data to a file
#             with open(xml_file_path, 'wb') as xml_file:
#                 xml_file.write(xml_data)
#
#
# def create_base_rule_dic(id, owner='system', kbid='', enable='t', ver='1', file_name='', filter_list={}, action={},
#                          regulation={}):
#     kbid = f'{id}_1'
#     payam_rule_dictionary = {
#         "rule": {
#             "@id": "",
#             "@owner": "",
#             "@kbid": "",
#             "@enable": "",
#             "@ver": "",
#             "@file_name": "",
#             "filter_list": {},
#             "action": {},
#             "regulation": {}
#         }
#     }
#     payam_rule_dictionary['rule']['@id'] = id
#     payam_rule_dictionary['rule']["@owner"] = owner
#     payam_rule_dictionary['rule']["@kbid"] = kbid
#     payam_rule_dictionary['rule']["@enable"] = enable
#     payam_rule_dictionary['rule']["@ver"] = ver
#     payam_rule_dictionary['rule']["@file_name"] = file_name
#     payam_rule_dictionary['rule']["filter_list"] = filter_list
#     payam_rule_dictionary['rule']["action"] = action
#     payam_rule_dictionary['rule']["regulation"] = regulation
#
#     return payam_rule_dictionary
#
#
# # filter
# def create_filter_list_dic():
#     filter_list = {
#         "filter": [
#
#         ]
#     }
#     return filter_list
#
#
# def element_of_filterlist_dic_source(ip_locatoin="ANY", reference_id='reference_id', reference_type='reference_type',
#                                      port="0-65535"):
#     source = {"ip": {"@location": "",
#                      "@reference_id": "",
#                      "@reference_type": "",
#                      }, "port": ""}
#
#     source['ip']["@location"] = ip_locatoin
#     source['ip']["@reference_id"] = reference_id
#     source['ip']["@reference_type"] = reference_type
#     source["port"] = port
#
#     return source
#
#
# def element_of_filterlist_dic_target(ip_locatoin="ANY", reference_id='reference_id', reference_type='reference_id',
#                                      port="0-65535"):
#     target = {"ip": {"@location": "",
#                      "@reference_id": "",
#                      "@reference_type": "",
#                      }, "port": ""}
#
#     target['ip']["@location"] = ip_locatoin
#     target['ip']["@location"] = reference_id
#     target['ip']["@location"] = reference_type
#     target["port"] = port
#     return target
#
#
# def element_of_filterlist_dic_flag_list(flag):
#     flag_list = {
#         "flag": ""
#     }
#     flag_list["flag"] = flag
#     return flag_list
#
#
# def filterlist_dic_event_list_tag_list(tag_list=[], meaning='meaning', text='text'):
#     temp = {
#         "@meaning": "",
#         "#text": ""
#     }
#     temp["@meaning"] = meaning
#     temp["#text"] = text
#     tag_list.append(temp)
#     return tag_list
#
#
# def element_of_filterlist_dic_event_list(sensor_type="ANY", class_type="", tag=[]):
#     event_list = {
#         "event": {
#             "@sensor_type": "ANY",
#             "@class_type": "",
#             "tag": []
#         }
#     }
#     event_list["event"]["@sensor_type"] = sensor_type
#     event_list["event"]["@class_type"] = class_type
#     event_list["event"]["tag"] = tag
#     return event_list
#
#
# def element_of_filterlist_dic(filter_list, id='1', name='name', occurrence='accurrence', weight='weigh',
#                               timeout='timeout',
#                               s_ip_locatoin="ANY", s_reference_id='s_reference_id', s_reference_type='s_reference_type',
#                               s_port="0-65535",
#                               t_ip_locatoin="ANY", t_reference_id='t_reference_id', t_reference_type='t_reference_type',
#                               t_port="0-65535",
#                               flag='flag', tag=[]):
#     filter_list = {
#         "@id": "",
#         "@name": "",
#         "@occurrence": "",
#         "@weight": "",
#         "@timeout": "",
#         "source": {},
#         "target": {},
#         "flag_list": {},
#         "event_list": {}
#     }
#     filter_list["@id"] = id
#     filter_list["@name"] = name
#     filter_list["@occurrence"] = occurrence
#     filter_list["@weight"] = weight
#     filter_list["@timeout"] = timeout
#
#     filter_list["source"] = element_of_filterlist_dic_source(s_ip_locatoin, s_reference_id, s_reference_type, s_port)
#     filter_list["target"] = element_of_filterlist_dic_target(t_ip_locatoin, t_reference_id, t_reference_type, t_port)
#     filter_list["flag_list"] = element_of_filterlist_dic_flag_list(flag=flag)
#     tag_list = list()
#     tag_list = filterlist_dic_event_list_tag_list(tag_list=tag, meaning='meaning', text='text')
#     filter_list["event_list"] = element_of_filterlist_dic_event_list(sensor_type="ANY", class_type="class_type",
#                                                                      tag=tag_list)
#
#     return filter_list
#
#
# # end of filter
#
#
# def create_action_alert_additional_data(alert_additional_data_list=[], meaning=" ", reference_id=" ")
#     temp = {
#         "@meaning": "",
#         "@reference_id": ""
#     }
#     temp["@meaning"] = meaning
#     temp["@reference_id"] = reference_id
#     alert_additional_data_list.append(temp)
#
#
# def create_action_alert(priority, category, message,
#                         source_ip_reference_id, source_ip_reference_type,
#                         target_ip_reference_id, target_ip_reference_type,
#                         additional_data
#                         ):
#     alert = {
#         "@priority": "",
#         "@category": "",
#         "message": "",
#         "source": {
#             "ip": {
#                 "@reference_id": "",
#                 "@reference_type": ""
#             }
#         },
#         "target": {
#             "ip": {
#                 "@reference_id": "",
#                 "@reference_type": ""
#             }
#         },
#         "additional_data": [
#             {
#                 "@meaning": "",
#                 "@reference_id": ""
#             },
#             {
#                 "@meaning": "",
#                 "@reference_id": ""
#             }
#         ]
#     }
#     alert["@priority"] = priority
#     alert["@category"] = category
#     alert["message"] = message
#     alert["source"]["ip"]["@reference_id"] = source_ip_reference_id
#     alert["source"]["ip"]["@reference_id"] = source_ip_reference_type
#     alert["source"]["ip"]["@reference_id"] = target_ip_reference_id
#     alert["source"]["ip"]["@reference_id"] = target_ip_reference_type
#     create_action_alert_additional_data(alert_additional_data_list=alert["additional_data"], meaning="meaning",
#                                         reference_id="reference_id ")
#     return alert
#
#
# # ...
# def create_action_prerequisite_predicate(paramlist=[], reference_type="reference_type"):
#     temp = {
#         "@reference_type": ""
#     }
#     temp["@reference_type"] = reference_type
#     paramlist.append()
#
#
# def create_action_prerequisite_predicate(type=" ", param=[]):
#     temp = {
#         "@type": "",
#         "param": []}
#     temp["@type"] = type
#     paramlist = []
#     temp["param"] = create_action_prerequisite_predicate(paramlist=paramlist, reference_type="reference_type1")
#     temp["param"] = create_action_prerequisite_predicate(paramlist=paramlist, reference_type="reference_type2")
#     return temp
#
#
# def create_action_prerequisite():
#     prerequisite = {
#         "predicate": [
#             # {
#             #     "@type": "Recon-Host",
#             #     "param": [
#             #         {
#             #             "@reference_type": "source.ip"
#             #         },
#             #         {
#             #             "@reference_type": "target.ip"
#             #         }
#             #     ]
#             # },
#             # {
#             #     "@type": "Recon-Network",
#             #     "param": {
#             #         "@reference_type": "source.ip"
#             #     }
#             # }
#         ]
#     }
#     prerequisite["predicate"]
#
#
# # ...
# def create_action_consequence(predicate_list=[], type="type", param_list=[]):
#     param_list_include_dic = []
#     for element in param_list:
#         temp_dic = {
#             "@reference_type": ""
#         }
#         temp_dic["@reference_type"]=element
#         param_list_include_dic.append(temp_dic)
#
#     temp = {
#         "@type": "",
#         "param": []
#     }
#
#     temp["@type"]= type
#     temp["param"]= param_list_include_dic
#
#     param_list.append(temp)
#
#
# def create_action_consequence():
#     consequence = {
#         "predicate": [
#             {
#                 "@type": "",
#                 "param": [
#                     {
#                         "@reference_type": ""
#                     },
#                     {
#                         "@reference_type": ""
#                     }
#                 ]
#             },
#             {
#                 "@type": "",
#                 "param": {
#                     "@reference_type": ""
#                 }
#             }
#         ]
#     }
#     consequence["predicate"]
#     return consequence
#
#
# def create_action_dic(alert, prerequisite, consequence):
#     action = {
#         "alert": {
#             "@priority": " ",
#             "@category": "",
#             "message": "",
#             "source": {
#                 "ip": {
#                     "@reference_id": "",
#                     "@reference_type": ""
#                 }
#             },
#             "target": {
#                 "ip": {
#                     "@reference_id": "",
#                     "@reference_type": ""
#                 }
#             }
#         },
#         "prerequisite": {
#             "predicate": [
#                 {
#                     "@type": "",
#                     "param": [
#                         {
#                             "@reference_type": ""
#                         },
#                         {
#                             "@reference_type": ""
#                         }
#                     ]
#                 },
#                 {
#                     "@type": "",
#                     "param": [
#                         {
#                             "@reference_type": ""
#                         },
#                         {
#                             "@reference_type": ""
#                         }
#                     ]
#                 }
#             ]
#         },
#         "consequence": {
#             "predicate": [
#                 {
#                     "@type": "",
#                     "param": [
#                         {
#                             "@reference_type": ""
#                         },
#                         {
#                             "@reference_type": ""
#                         }
#                     ]
#                 },
#                 {
#                     "@type": "",
#                     "param": {
#                         "@reference_type": ""
#                     }
#                 }
#             ]
#         }
#     }
#
#     action["alert"] = alert
#     action["prerequisite"] = prerequisite
#     action["consequence"] = consequence
#
#     return action
#
# # regulation
# def create_regulation_add_filter(filter_list=[], id_list=[]):
#     for id in id_list:
#         temp = {"@id":""}
#         temp["@id"]=id
#         filter_list.append(temp)
#
# def create_regulation_add_group_list(sequence_or_filter_list, filterlist):
#     for filter in filterlist:
#         temp = {"filter":""}
#         temp["filter"]=filter
#         sequence_or_filter_list.append(filter)
#
# def create_regulation_dic():
#     regulation = {
#         "sequence": {
#             # "filter": {
#             #     "@id": "1"
#             # },
#             # "group": [
#             #     {
#             #         "filter": [
#             #             {
#             #                 "@id": "2"
#             #             },
#             #             {
#             #                 "@id": "3"
#             #             }
#             #         ]
#             #     },
#             #     {
#             #         "filter": [
#             #             {
#             #                 "@id": "4"
#             #             },
#             #             {
#             #                 "@id": "5"
#             #             }
#             #         ]
#             #     }
#             # ]
#         }
#     }
#     regulation["sequence"]
#
#     return regulation
#
#
# def main():
#     # extract_sigma_rules()
#     # convert_yaml_to_json()
#     # convert_json_to_xml()
#
#     # create filterlist part
#     filerlist = create_filter_list_dic()
#     filter_temp = element_of_filterlist_dic(filter_list=filerlist, id='1', name='name', occurrence='accurrence',
#                                             weight='weigh',
#                                             timeout='timeout',
#                                             s_ip_locatoin="ANY", s_reference_id='s_reference_id',
#                                             s_reference_type='s_reference_type',
#                                             s_port="0-65535",
#                                             t_ip_locatoin="ANY", t_reference_id='t_reference_id',
#                                             t_reference_type='t_reference_type',
#                                             t_port="0-65535",
#                                             flag='flag', tag=[])
#
#     # create action part
#     action_temp = {}
#
#     # create regulation part
#     regulation_temp = {}
#
#     rule = create_base_rule_dic(id="10002", owner="system", kbid="10002_1", enable="t", ver="1", file_name='filtername',
#                                 filter_list=filter_temp, action=action_temp, regulation=regulation_temp)
#     print(rule)
#
#     main()

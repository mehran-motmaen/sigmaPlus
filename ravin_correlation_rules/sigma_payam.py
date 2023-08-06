# "{0CCE9217-69AE-11D9-BED3-505054503030}": {"EventIDs": [4625], "Name": "Audit Account Lockout"},

main_dictionary = {}

payam_rule_dictionary = {
  "rule": {
    "@id": "",
    "@owner": "",
    "@kbid": "",
    "@enable": "",
    "@ver": "",
    "@file_name": "",
    "filter_list": {
      "filter": [
        {
          "@id": "",
          "@name": "",
          "@weight": "",
          "source": {
            "ip": {
              "@location": ""
            },
            "port": ""
          },
          "target": {
            "ip": {
              "@location": ""
            },
            "port": ""
          },
          "event_list": {
            "event": {
              "@sensor_type": "",
              "@class_type": "",
              "tag": [
                {
                  "@meaning": "",
                  "#text": ""
                },
                {
                  "@meaning": "",
                  "#text": ""
                },
                {
                  "@meaning": "",
                  "#text": ""
                }
              ]
            }
          }
        },
        {
          "@id": "",
          "@name": "",
          "@occurrence": "",
          "@weight": "",
          "@timeout": "",
          "source": {
            "ip": {
              "@reference_id": "",
              "@reference_type": ""
            },
            "port": ""
          },
          "target": {
            "ip": {
              "@reference_id": "",
              "@reference_type": ""
            },
            "port": ""
          },
          "flag_list": {
            "flag": ""
          },
          "event_list": {
            "event": {
              "@sensor_type": "",
              "@class_type": "",
              "tag": [
                {
                  "@meaning": "",
                  "#text": ""
                },
                {
                  "@meaning": "",
                  "#text": ""
                },
                {
                  "@meaning": "",
                  "#text": ""
                }
              ]
            }
          }
        },
        {
          "@id": "",
          "@name": "",
          "@occurrence": "",
          "@weight": "",
          "@timeout": "",
          "source": {
            "ip": {
              "@reference_id": "",
              "@reference_type": ""
            },
            "port": ""
          },
          "target": {
            "ip": {
              "@reference_id": "",
              "@reference_type": ""
            },
            "port": ""
          },
          "flag_list": {
            "flag": ""
          },
          "event_list": {
            "event": {
              "@sensor_type": "",
              "@class_type": "",
              "tag": [
                {
                  "@meaning": "",
                  "#text": ""
                },
                {
                  "@meaning": "",
                  "#text": ""
                },
                {
                  "@meaning": "",
                  "#text": ""
                }
              ]
            }
          }
        },
        {
          "@id": "",
          "@name": "",
          "@occurrence": "",
          "@weight": "",
          "@timeout": "",
          "source": {
            "ip": {
              "@reference_id": "",
              "@reference_type": ""
            },
            "port": ""
          },
          "target": {
            "ip": {
              "@reference_id": "",
              "@reference_type": ""
            },
            "port": ""
          },
          "flag_list": {
            "flag": ""
          },
          "event_list": {
            "event": {
              "@sensor_type": "",
              "@class_type": "",
              "tag": [
                {
                  "@meaning": "",
                  "#text": ""
                },
                {
                  "@meaning": "",
                  "#text": ""
                },
                {
                  "@meaning": "",
                  "#text": ""
                }
              ]
            }
          }
        }
      ]
    },
    "action": {
      "alert": {
        "@priority": "",
        "@category": "",
        "message": "",
        "source": {
          "ip": {
            "@reference_id": "",
            "@reference_type": ""
          }
        },
        "target": {
          "ip": {
            "@reference_id": "",
            "@reference_type": ""
          }
        }
      },
      "prerequisite": {
        "predicate": [
          {
            "@type": "",
            "param": [
              {
                "@reference_type": ""
              },
              {
                "@reference_type": ""
              }
            ]
          },
          {
            "@type": "",
            "param": [
              {
                "@reference_type": ""
              },
              {
                "@reference_type": ""
              }
            ]
          }
        ]
      },
      "consequence": {
        "predicate": [
          {
            "@type": "",
            "param": [
              {
                "@reference_type": ""
              },
              {
                "@reference_type": ""
              }
            ]
          },
          {
            "@type": "",
            "param": {
              "@reference_type": ""
            }
          }
        ]
      }
    },
    "regulation": {
      "sequence": {
        "filter": [
          {
            "@id": ""
          },
          {
            "@id": ""
          },
          {
            "@id": ""
          },
          {
            "@id": ""
          }
        ]
      }
    }
  }
}

payam_rule_dictionary2 = {
  "rule": {
    "@id": "",
    "@owner": "",
    "@kbid": "",
    "@enable": "",
    "@ver": "",
    "@file_name": "",
    "filter_list": { },
    "action": {},
    "regulation": {}
  }
}
# ........filter_list........
filter_list= {
      "filter": [
        {
          "@id": "",
          "@name": "",
          "@weight": "",
          "source": {},
          "target": {},
          "event_list": {}
        },
        {
          "@id": "",
          "@name": "",
          "@occurrence": "",
          "@weight": "",
          "@timeout": "",
          "source": {},
          "target": {},
          "flag_list": {},
          "event_list": {}
        },
      ]
    }
# ........action........

action= {
      "alert": {
        "@priority" : " ",
        "@category": "",
        "message": "",
        "source": {
          "ip": {
            "@reference_id": "",
            "@reference_type": ""
          }
        },
        "target": {
          "ip": {
            "@reference_id": "",
            "@reference_type": ""
          }
        }
      },
      "prerequisite": {
        "predicate": [
          {
            "@type": "",
            "param": [
              {
                "@reference_type": ""
              },
              {
                "@reference_type": ""
              }
            ]
          },
          {
            "@type": "",
            "param": [
              {
                "@reference_type": ""
              },
              {
                "@reference_type": ""
              }
            ]
          }
        ]
      },
      "consequence": {
        "predicate": [
          {
            "@type": "",
            "param": [
              {
                "@reference_type": ""
              },
              {
                "@reference_type": ""
              }
            ]
          },
          {
            "@type": "",
            "param": {
              "@reference_type": ""
            }
          }
        ]
      }
    }

# ........regulation........
regulation = {
      "sequence": {
        "filter": [
          {
            "@id": ""
          },
          {
            "@id": ""
          },
          {
            "@id": ""
          },
          {
            "@id": ""
          }
        ]
      }
    }

# ........finish........


sigma_payam_dic = {
    'title':'',
    'id' : '',
    'status': '',
    'description': '',
    'references': '',
    'author': '',
    'date': '',
    'modified': '',
    'tags': '',
    'logsource': '',
    # 'category': '',
    # 'product': '',
    'detection': '',
    # 'keywords': '',
    # 'condition': '',
    # 'falsepositives': '',
    'falsepositives': '',
    'level': '',
    'fields': '',
    'related': '',
    'analysis': '',
    'tag': '',

}

title_sigma_payam = {}
id_sigma_payam = {}
status_sigma_payam = {}
description_sigma_payam = {}
references_sigma_payam = {}
author_sigma_payam = {}
date_sigma_payam = {}
tags_sigma_payam = {}
logsource_sigma_payam = {}
category_sigma_payam = {}
product_sigma_payam = {}
definition_sigma_payam = {}
detection_sigma_payam = {}
keywords_sigma_payam = {}
condition_sigma_payam = {}
falsepositives_sigma_payam = {}
level_sigma_payam = {}
detection_sigma_payam = {}




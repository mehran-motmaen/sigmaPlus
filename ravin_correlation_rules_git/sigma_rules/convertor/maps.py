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
    'falsepositives': '',
    'level': '',
    'fields': '',
    'related': '',
    'analysis': '',
    'tag': '',

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
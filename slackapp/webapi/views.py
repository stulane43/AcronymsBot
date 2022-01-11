
class Views:

    def __init__(self, connector):
        self.connector = connector.details

    def appHomeView(self, authenticated):
        '''
        Main Home Tab view for authorized users
        '''
        try:
            if authenticated[0] == True:
                view = 	{
                    "type": "home",
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"*Hi @{authenticated[1].data['user']['name']}, Welcome to Acronyms*  :memo: \n\n This app allows you to search terms related to your business and look up their associated `definitions` and/or `descriptions`."
                            },
                            "accessory": {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Learn More",
                                    "emoji": True
                                },
                                "value": "click_me_123",
                                "action_id": "learnMore"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "\n\n"
                            }
                        },
                        {
                            "type": "actions",
                            "elements": [
                                {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":clipboard: View All Acronyms",
                                        "emoji": True
                                    },
                                    "style": "primary",
                                    "value": "click_me_123",
                                    "action_id": "viewAllAcronyms"
                                }
                            ]
                        },
                        {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": "Acronym Search  :book:",
                                "emoji": True
                            }
                        },
                        {
                            "type": "divider"
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "\n\n"
                            }
                        },
                        {
                            "dispatch_action": True,
                            "type": "input",
                            "element": {
                                "type": "plain_text_input",
                                "action_id": "acronymsearch",
                                "placeholder": {
                                    "type": "plain_text",
                                    "text": " "
                                }
                            },
                            "label": {
                                "type": "plain_text",
                                "text": " ",
                                "emoji": True
                            }
                        }
                    ]
                }
                return view
            else:
                view = self.unauthorized_homeView(authenticated[1]['user']['name'])
                return view
        except Exception as e:
            print(Exception(e))

    def unauthorized_homeView(self, username):
        '''
        Home Tab view for unauthorized user
        '''
        view={
        "type":"home",
        "blocks":[
                {
                    "type":"section",
                    "text":{
                    "type":"mrkdwn",
                    "text":f"Hi @{username}, You do not have access to this Slack App."
                    }
                }
            ]
        }
        return view

    def learnMoreModal(self):
        view = {
            "type": "modal",
            "close": {
                "type": "plain_text",
                "text": "Back",
                "emoji": True
            },
            "title": {
                "type": "plain_text",
                "text": "Acronyms",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": "Created By: stulane43"
                        }
                    ]
                },
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":book:  Summary",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Acronyms* is a tool that you can use to look up terms and/or abbreviations used throughout your business."
                    }
                },
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":small_orange_diamond:Available Controls:small_orange_diamond:",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":clipboard:  *View All Acronyms* \n        •  View a complete list of all acronyms and their \n            definitions/descriptions"
                    }
                },
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":small_orange_diamond:Available Slash Commands:small_orange_diamond:",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ">`/acronym help` ```View available slash commands```\n\n>`/acronym [acronym]` ```View the definition/description of an acronym```\n\n>`/acronym all` ```View a complete list of all acronyms and their definitions/descriptions```\n\n*Go to <#ChannelID> to request additions/edits to Acronyms*"
                    }
                }
            ]
        }
        return view

    def learnMoreModalV2(self):
        view = {
            "type": "modal",
            "close": {
                "type": "plain_text",
                "text": "Back",
                "emoji": True
            },
            "title": {
                "type": "plain_text",
                "text": "Acronyms",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": "Created By: stulane43"
                        }
                    ]
                },
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":book:  Summary",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Acronyms* is a tool that you can use to look up terms and/or abbreviations used throughout your business."
                    }
                },
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":small_orange_diamond:Available Controls:small_orange_diamond:",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":clipboard:  *View All Acronyms* \n        •  View a complete list of all acronyms and their \n            definitions/descriptions"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":heavy_plus_sign:  *Add Acronym Request* \n        •  Submit a request to add an acronym to *Acronyms*\n        •  Enter the Acronymn you wish to add with its\n            definition/description\n        •  Once reviewed, you will receive an approval/denied \n            notification inside the messages tab on Acronyms"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":heavy_minus_sign:  *Update Acronym Request* \n        •  Submit a request to update an acronym's definition and/or\n            description\n        •  Enter the Acronymn you wish to update with its new\n            definition/description \n        •  Once reviewed, you will receive an approval/denied \n            notification inside the messages tab on Acronyms"
                    }
                },
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":small_orange_diamond:Available Slash Commands:small_orange_diamond:",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ">`/acronym [acronym]` View the definition/description of an acronym _Ex._ `/acronym AP`\n>`/acronym add` Submit a request to add an acronym \n>`/acronym edit` Submit a request to edit an acronym's definition/description"
                    }
                }
            ]
        }
        return view

    def acronymView(self, username, acronym):
        if acronym['found'] == True:
            view = {
                "type": "home",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*Hi @{username}, Welcome to Acronyms*  :memo: \n\n This app allows you to search terms related to your business and look up their associated `definitions` and/or `descriptions`."
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Learn More",
                                "emoji": True
                            },
                            "value": "click_me_123",
                            "action_id": "learnMore"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n\n"
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": ":clipboard: View All Acronyms",
                                    "emoji": True
                                },
                                "style": "primary",
                                "value": "click_me_123",
                                "action_id": "viewAllAcronyms"
                            }
                        ]
                    },
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Search Acronym  :book:",
                            "emoji": True
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "acronymsearch",
                            "placeholder": {
                                "type": "plain_text",
                                "text": " "
                            }
                        },
                        "label": {
                            "type": "plain_text",
                            "text": " ",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n\n"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n\n"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n\n"
                        }
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": f"Acronym Searched: `{acronym['acronym']}`"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*`{acronym['acronym']}`* {acronym['definition']}{acronym['description']}"
                        }
                    }
                ]
            }
        else:
            view = self.acronymNotFoundView(username, acronym['acronym'])
        return view
    
    def acronymNotFoundView(self, username, acronym):
        view = {
            "type": "home",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Hi @{username}, Welcome to Acronyms*  :memo: \n\n This app allows you to search terms related to your business and look up their associated `definitions` and/or `descriptions`."
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Learn More",
                            "emoji": True
                        },
                        "value": "click_me_123",
                        "action_id": "learnMore"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "\n\n"
                    }
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": ":clipboard: View All Acronyms",
                                "emoji": True
                            },
                            "style": "primary",
                            "value": "click_me_123",
                            "action_id": "viewAllAcronyms"
                        }
                    ]
                },
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "Search Acronym  :book:",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "dispatch_action": True,
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "acronymsearch",
                        "placeholder": {
                            "type": "plain_text",
                            "text": " "
                        }
                    },
                    "label": {
                        "type": "plain_text",
                        "text": " ",
                        "emoji": True
                    }
                },
                                    {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "\n\n"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "\n\n"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "\n\n"
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": f"Acronym Searched: `{acronym}`"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Acronym Not Found  :disappointed:*"
                    }
                },
                {
                "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ">If you would like to add this abbreviation to Acronyms, send a message in <#ChannelID>"
                    }
                }
            ]
        }
        return view
    
    def scAcronymView(self, acronym):
        if acronym['found'] == True:
            view = {
                "blocks": [
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": f"Acronym Searched: `{acronym['acronym']}`"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*`{acronym['acronym']}`* {acronym['definition']}{acronym['description']}"
                        }
                    }
                ]
            }
        else:
            view = self.scAcronymNotFoundView(acronym)
        return view
    
    def scAcronymNotFoundView(self, acronym):
        view = {
                "blocks": [
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": f"Acronym Searched: `{acronym['acronym']}`"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Acronym Not Found  :disappointed:*"
                        }
                    },
                    {
                    "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": ">If you would like to add this abbreviation to Acronyms, send a message in \n><#ChannelID>"
                        }
                    }
                ]
            }
        return view
    
    def scHelpView(self):
        view = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Acronyms Help Menu  :book:*"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ">`/acronym [acronym]` View the definition/description of an acronym - _Ex._ `/acronym AD`\n>`/acronym all` View a complete list of all acronyms and their definitions/descriptions\n>Go to <#ChannelID> to request additions/edits to Acronyms"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Visit <https://DOMAIN.slack.com/archives/APPCHANNELID|Acronyms> to learn more!*"
                    }
                }
            ]
        }
        return view
    
    def scAllAcronymsView(self, allAcronyms):
        view = {
            "attachments": [
                {
                    "color": "#FFA500",
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "*All Available Acronyms  :book:*"
                            }
                        },
                        {
                            "type": "divider"
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"{allAcronyms[0]}"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"{allAcronyms[1]}"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"{allAcronyms[2]}"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"{allAcronyms[3]}"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"{allAcronyms[4]}"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"{allAcronyms[5]}"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"{allAcronyms[6]}"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"{allAcronyms[7]}"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"{allAcronyms[8]}"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"{allAcronyms[9]}"
                            }
                        }                                                                                                                                                                                                                
                    ]
                }
            ]
        }
        return view        
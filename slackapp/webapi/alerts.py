
def unauthorizedAlert(user_info):
    '''
    Unauthorized user alert message
    '''
    message = {
        "attachments": [
            {
                "color": "#800000",
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Unathorized User Alert"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f">*Member:* @{user_info.data['user']['name']} \n>*User Id:* {user_info.data['user']['id']} \n> *Action:* Attempted to view the Home Tab"
                        }
                    }
                ]
            }
        ]
    }
    return message
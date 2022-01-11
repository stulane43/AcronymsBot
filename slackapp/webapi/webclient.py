from slack_sdk import WebClient

class Client:

    def __init__(self, app_token):
        self.client = WebClient(token=app_token)
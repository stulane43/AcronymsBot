from .webclient import Client
import requests

class Chat(Client):

    def __init__(self, app_token):
        super().__init__(app_token)

    def chatPostMessage(self, channelID, message):
        try:
            self.client.chat_postMessage(channel=channelID, attachments=message['attachments'])
        except Exception as e:
            print(Exception(e))
            
    def postWebhookMessage(self, message, webhook):
        requests.post(url=webhook, json=message)
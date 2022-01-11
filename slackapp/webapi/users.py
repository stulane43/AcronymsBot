from .webclient import Client

class Users(Client):

    def __init__(self, app_token):
        super().__init__(app_token)

    def usersInfo(self, event):
        try:
            response = self.client.users_info(user=event['user'])
            return response
        except Exception as e:
            print(Exception(e))
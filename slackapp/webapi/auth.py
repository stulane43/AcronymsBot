from .users import Users
from .chat import Chat
import slackapp.webapi.alerts as alerts

class Auth(Users, Chat):

    def __init__(self, connector, app_token):
        super().__init__(app_token)
        self.conn = connector.details
    
    def authenticateUser(self, event):
        '''
        Authenticates Slack user to App Home Surface
        '''
        try:
            user_info = self.usersInfo(event)
            # if event['user'] not in self.conn['approvedUsers']:
            #     unauthMessage = alerts.unauthorizedAlert(user_info)
            #     self.chatPostMessage(channelID=self.conn['unauthorizedChannel'], message=unauthMessage)
            #     return False, user_info
            # else:
            return True, user_info
        except Exception as e:
            print(Exception(e))
from slackapp.webapi.auth import Auth
from slackapp.webapi.views import Views
from acronyms import Acronyms

class Events(Auth, Views):

    def __init__(self, connector, app_token):
        super().__init__(connector, app_token)
        self.log = connector.log
        self.acronyms = Acronyms()

    def getAppHome(self, event):
        try:
            authenticated = self.authenticateUser(event)
            appHomeView = self.appHomeView(authenticated)
            return {'view': appHomeView, 'userId': authenticated[1].data['user']['id']}
        except Exception as e:
            self.log.error(f'***Events-Error*** getAppHome: {e}')
            
    def getLearnMoreModal(self):
        modal = self.learnMoreModal()
        return modal
    
    def getAllAcronyms(self, body):
        try:
            userid = body["user"]["id"]
            allAcronyms = self.acronyms.getAllAcronyms()
            view = self.scAllAcronymsView(allAcronyms)
            self.chatPostMessage(channelID=userid, message=view)        
        except Exception as e:
            self.log.error(f'***Events-Error*** getAllAcronyms: {e}')

    def getAcronymResults(self, body):
        username = body["user"]["username"]
        userid = body["user"]["id"]
        acronymSearched = body['actions'][0]['value']
        acronym = self.acronyms.searchAcronym(acronymSearched.upper())
        acronymView = self.acronymView(username, acronym)
        return {'view': acronymView, 'userId': userid, 'username': username}
    
    def scAcronymnSearch(self, body):
        acronymSearched = body['text']
        acronym = self.acronyms.searchAcronym(acronymSearched.upper())
        acronymnView = self.scAcronymView(acronym)
        return acronymnView
        
    def scAcronymHandler(self, body):
        command = body['text'].strip()
        if command.upper() == '':
            view = self.scHelpView()
        elif command.upper() == 'HELP':
            view = self.scHelpView()
        elif command.upper() == 'ALL':
            allAcronyms = self.acronyms.getAllAcronyms()
            view = self.scAllAcronymsView(allAcronyms)
        else:
            view = self.scAcronymnSearch(body)
        self.postWebhookMessage(message=view, webhook=body['response_url'])
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slackapp.connector import Connector
from slackapp import Events

connector = Connector(__name__)
app = App(token=connector.details['botToken'], signing_secret=connector.details['signingSecret'])
eventHandler = Events(connector, app_token=app._token)

@app.event("app_home_opened")
def appHomeOpened(client, event):
    '''
    Visualize App Home Surface
    '''
    try:
        home = eventHandler.getAppHome(event)
        client.views_publish(user_id=home['userId'], view=home['view'])
    except Exception as e:
        connector.log.error(f'***App-Error*** appHomeOpened: {e}')
        
@app.action("learnMore")
def learnMoreModal(ack, body, client):
    try:
        ack()
        modalView = eventHandler.getLearnMoreModal()
        client.views_open(trigger_id=body['trigger_id'], view_id=body['view']['id'], hash = body["view"]["hash"], notify_on_close = True, view=modalView)
    except Exception as e:
        connector.log.error(f'***App-Error*** learnMoreModal: {e}')

@app.action("viewAllAcronyms")
def allAcronymsModal(ack, body, client):
    try:
        ack()
        eventHandler.getAllAcronyms(body)
    except Exception as e:
        connector.log.error(f'***App-Error*** allAcronymsModal: {e}')
        
@app.action("acronymsearch")
def acronymSearch(ack, body, client):
    try:
        ack()
        results = eventHandler.getAcronymResults(body)
        client.views_publish(user_id=results['userId'], view=results['view'])
    except Exception as e:
        connector.log.error(f'***App-Error*** acronymnSearch: {e}')
        
@app.command("/acronym")
def acronymnSlashCommand(ack, body):
    try:
        ack()
        eventHandler.scAcronymHandler(body)
    except Exception as e:
        connector.log.error(f"***App-Error*** acronymnSlashCommand: {e}")

def run():
    connector.log.info("Started Bolt app!")
    SocketModeHandler(app, connector.details['appToken']).start()
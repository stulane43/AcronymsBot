import json
from .logger import Logger

class Connector(Logger):

    # Instances a connector object.
    # Allows easier resuse rather than loading the
    # json file for each sub-API.
    def __init__(self, name, debug=False):
        super().__init__(name, debug)
        self.details = json.load(open('configuration/config.json'))
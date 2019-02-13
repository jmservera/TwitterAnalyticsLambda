
import os

class __settings:
    def __init__(self):
        terms=os.getenv("TRACK_TERMS","trump,clinton,sanders,hillary clinton,bernie,donald trump")
        self.TRACK_TERMS = terms.split(",")
        self.TWITTER_KEY=os.environ["TWITTER_KEY"]
        self.TWITTER_SECRET=os.environ["TWITTER_SECRET"]
        self.TWITTER_APP_KEY=os.environ["TWITTER_APP_KEY"]
        self.TWITTER_APP_SECRET=os.environ["TWITTER_APP_SECRET"]
        self.EVENTHUBS_CONNECTIONSTRING=os.environ["EVENTHUBS_CONNECTIONSTRING"]
        self.WEB_PORT=int(os.getenv("WEB_PORT","80"))
            
        print ("Settings initialized.\nTRACK_TERMS: {0}\nWEB_PORT: {1}".format(self.TRACK_TERMS, self.WEB_PORT))

Settings=__settings()

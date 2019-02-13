from streamlistener import StreamListener
import tweepy
from settings import Settings
from send import EventHubSender
import webapp
import threading



httpd=webapp.HTTPServer(('0.0.0.0',Settings.WEB_PORT),webapp.web_server)
thread= threading.Thread(target= httpd.serve_forever)
thread.daemon=True
thread.start()
print("HTTPServer started in port {0}".format(Settings.WEB_PORT))

auth = tweepy.OAuthHandler(Settings.TWITTER_APP_KEY, Settings.TWITTER_APP_SECRET)
auth.set_access_token(Settings.TWITTER_KEY, Settings.TWITTER_SECRET)
api = tweepy.API(auth)

stream_listener = StreamListener(output=EventHubSender(Settings.EVENTHUBS_CONNECTIONSTRING))
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=Settings.TRACK_TERMS)

httpd.shutdown()

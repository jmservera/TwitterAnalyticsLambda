from tweepy import StreamListener as _streamListener
from textblob import TextBlob
import json
from telemetry import Telemetry

class StreamListener(_streamListener):

    def __init__(self, output=None):
        self.output=output
        super(StreamListener,self).__init__()

    def on_status(self, status):
        if status.retweeted:
            return
        
        Telemetry.IncrementTweets()

        description = status.user.description
        loc = status.user.location
        text = status.text
        coords = status.coordinates
        geo = status.geo
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color
        blob = TextBlob(text)
        sent = blob.sentiment

        if geo is not None:
            geo = json.dumps(geo)

        if coords is not None:
            coords = json.dumps(coords)

        if not self.output:
            print(text)
        else:
            self.output.sendTweet({"id":id_str, "created_at":created,"text":text})

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
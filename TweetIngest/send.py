import sys
import logging
import datetime
import time
import os

import enhancedjsonencoder

from azure.eventhub import EventHubClient, Sender, EventData

from telemetry import Telemetry

class EventHubSender(object):
    def __init__(self, connectionString):
        print("Initiating EventHubSender with "+connectionString)
        if not connectionString:
            raise ValueError("No EventHubs URL supplied.")
        self.address=connectionString
        self.client=EventHubClient.from_connection_string(connectionString)
        self.sender=self.client.add_sender()
        self.client.run()
        self.encoder=enhancedjsonencoder.EnhancedJSONEncoder()

    def __del__(self):
        self.sender.close()

    def close(self):
        self.__del__()
    
    def sendTweet(self,tweet):
        try:
            tweetjson= self.encoder.encode(tweet)
            self.sender.send(EventData(tweetjson))
            Telemetry.IncrementMessages()
        except:
            raise



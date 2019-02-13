class __telemetry(object):

    def __init__(self):
        self._receivedTweets=0
        self._sentMessages=0

    @property
    def ReceivedTweets(self):
        return self._receivedTweets

    def IncrementTweets(self):
         self._receivedTweets=self._receivedTweets+1
         return self._receivedTweets

    @property
    def SentMessages(self):
        return self._sentMessages

    def IncrementMessages(self):
        self._sentMessages=self._sentMessages+1
        return self._sentMessages

Telemetry=__telemetry()


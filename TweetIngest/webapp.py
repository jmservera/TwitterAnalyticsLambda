from http.server import HTTPServer, BaseHTTPRequestHandler
from send import EventHubSender
from string import Formatter
from telemetry import Telemetry
from settings import Settings

class web_server(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.end_headers()
            file="<html><body><div>Filter: {2}</div><div>Received Tweets: {0}<br>Sent Messages:{1}</div></body></html>"
            page=file.format(Telemetry.ReceivedTweets,Telemetry.SentMessages,Settings.TRACK_TERMS)
            self.wfile.write(bytes(page,'utf-8'))
        except Exception as e:
            print(e)
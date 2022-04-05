from channels.generic.websocket import WebsocketConsumer
import json


class StoreConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({'message_from_server': 'Hello, client!'}))

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        print(text_data_json)

    def disconnect(self, message):
        pass

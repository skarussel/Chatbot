import configparser as cfg
import requests
import json

class TelegramChatbot:
    def __init__(self, token_path):
        parser=cfg.ConfigParser()
        parser.read(token_path)
        token=parser.get('credentials','token')
        self.base = base="https://api.telegram.org/bot{}/".format(token)
    
    def get_update(self,offset=0):
        r = requests.get(self.base+"getUpdates?offset={}".format(offset))
        result=json.loads(r.content)["result"]
        return result

    def send_message(self,msg,sender):
        url=self.base + "sendMessage?chat_id={}&text={}".format(sender, msg)
        if (msg is not None):
            requests.get(url)

    def send_anmiation(self,sender):
        animation_id="AQADU70Pki4AA8AMAAI"
        url=self.base + "sendAnimation?chat_id={}&animation={}".format(sender,animation_id)
        requests.get(url)
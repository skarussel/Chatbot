import configparser as cfg
import requests
import json

class TelegramChatbot:
    """ 
    Diese Klasse stellt Verbindung zur Telegram Chatbot API bereit. 
      
    Attributes: 
        base (string): Der Link, über den sich zur Chatbot Schnittstelle verbunden werden kann. 
    """
    
    def __init__(self, token_path):
        """
        Der Konstruktur benötigt den Pfad zu einer config.cfg, die 
        in der Sektion "credentials" den Autorisierungstoken für die Nutzung
        des Telegram Chatbots enthält.
        """
        
        parser=cfg.ConfigParser()
        parser.read(token_path)
        token=parser.get('credentials','token')
        self.base = base="https://api.telegram.org/bot{}/".format(token)
    
    def get_update(self,offset=0):
        """ 
        Diese Funktion liefert alle neuen Nachrichten an den Bot,
        wobei das Offset einer Message_ID entspricht,
        die angibt, ab welcher Nachricht gefiltert wird.
        """
        
        r = requests.get(self.base+"getUpdates?offset={}".format(offset))
        result=json.loads(r.content)["result"]
        return result

    def send_message(self,msg,sender):
        """ 
        Diese Funktion sendet eine Nachricht (msg) an einen Empfänger (sender).
        """
        
        url=self.base + "sendMessage?chat_id={}&text={}".format(sender, msg)
        if (msg is not None):
            requests.get(url)

    def send_anmiation(self,sender):
        """ 
        Diese Funktion soll eine Animation an einen Empfänger (sender) senden,
        tut dies aber noch nicht.
        """
        
        animation_id="AQADU70Pki4AA8AMAAI"
        url=self.base + "sendAnimation?chat_id={}&animation={}".format(sender,animation_id)
        requests.get(url)

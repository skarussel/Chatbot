from ConversationHandler import ConversationHandler
from DB import DB
from TelegramChatbot import TelegramChatbot

def get_user_state(db,users,user_id):
    """ 
    Diese Methode schaut in einem Dictionary (users) nach,
    bei welchem Zustand in der Konversation sich ein 
    Nutzer (user_id) derzeitig befindet. 
    """
    
    if (user_id not in users):
        users[user_id]=0
        
    elif (users[user_id]==901):
        return 901

    if (not db.user_exists(user_id)):
        users[user_id]=900
    return users[user_id]


def update_user_state(user_id,users,state):
    """ 
    Diese Methode aktualisiert den Zustand der Konversation eines 
    Users im users Dictionary. 
    """
    
    users[user_id]=state

# Der Server startet hier 
print('Coco has been started')

""" 
db: Ein Objekt der Datenbank
conversation: Ein Objekt des ConversationHandlers
chat: Ein Objekt des TelegramChatbots
uid: Die aktuelle update_id eines Eintrags
user_state: Ein Dicitonary, was jedem Nutzer einen Zustand 
der aktuellen Konversaion zuweist
state: Der Zustand, der den aktuellen Nutzer betrifft
"""

db=DB('db.json')
conversation=ConversationHandler()
chat = TelegramChatbot('config.cfg')
uid=None
user_state={}
state=0

for user in db.select_all():
    """ 
    An dieser Stelle wird allen usern der Datenbank
    eine Nachricht gesendet. Später sollen Nutzer in
    bestimmten Zeitintervallen angeschrieben werden.
    """
    
    msg = conversation.current_message(state)
    chat.send_message(msg, user['USER_ID'])

while True:
    """ 
    In dieser Dauerschleife wird der Telegram Chatbot
    nach neuen Nachrichten befragt.
    Falls eine neue nichtleere Nachricht empfangen wird,
    wird basierend auf dem Zustand eine Nachricht versendet
    """
    
    results=chat.get_update(uid)
    if results:
        for item in results:
            uid = item["update_id"]+1
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            sender = item["message"]["from"]["id"]
            state = get_user_state(db,user_state,sender)
            if message is not None:
                if (state==901):
                    db.insert(sender,message)
                    state=0
                    update_user_state(sender,user_state,state)
                    msg = conversation.current_message(state)
                    chat.send_message(msg, sender)
                    
                else:        
                    state, reply = conversation.update(message,state)
                    chat.send_message(reply, sender)
                    update_user_state(sender,user_state,state)

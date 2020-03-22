from ConversationHandler import ConversationHandler
from DB import DB
from TelegramChatbot import TelegramChatbot

def get_user_state(db,users,user_id):
    
    if (user_id not in users):
        users[user_id]=0
        
    elif (users[user_id]==901):
        return 901

    if (not db.user_exists(user_id)):
        users[user_id]=900
    return users[user_id]


def update_user_state(user_id,users,state):
    users[user_id]=state


    
print('Coco has been started')

db=DB('db.json')
conversation=ConversationHandler()
chat = TelegramChatbot('config.cfg')
uid=None
user_state={}
state=0
for user in db.select_all():
    msg = conversation.current_message(state)
    chat.send_message(msg, user['USER_ID'])

while True:
    
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
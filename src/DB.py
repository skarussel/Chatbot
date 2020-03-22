from tinydb import TinyDB,Query
class DB():
    def __init__(self, db_path):
        self.db_path=db_path
        
    def select_all(self):
        db = TinyDB(self.db_path)
        return db.all()
    
    def select_user(self,user_id):
        db = TinyDB(self.db_path)
        User=Query()
        return db.search(User.USER_ID == user_id)
    
    def insert(self, user_id,name):
        db = TinyDB(self.db_path)
        db.insert({'USER_ID': user_id,'USER':name,'AGE':10})
    
    def remove_all(self):
        db = TinyDB(self.db_path)
        db.purge()
        
    
    def user_exists(self,user_id):
        db = TinyDB(self.db_path)
        User=Query()
        result = db.search(User.USER_ID==user_id)
        if result:
            return True
        return False
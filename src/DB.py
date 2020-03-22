from tinydb import TinyDB, Query


class DB():
    """
   Diese Klasse verwaltet eine TinyDB Datenbank.

   Attributes:
       db (TinyDB): Eine TinyDB Datenbank, die im JSON Format verwaltet wird.
   """


def __init__(self, db_path):
    """
    Der Konstruktur erzeugt eine Datenbank im JSON Format,
    im übergebenen Pfad oder stellt eine Verbindung zu diesem her,
    falls beim Pfad bereits ein Datenbankobjekt existiert.
    """

    self.db = TinyDB(db_path)


def select_all(self):
    """
    Diese Funktion gibt alle Einträge der Datenbank als Liste zurück
    """

    return self.db.all()


def select_user(self, user_id):
    """
    Diese Funktion gibt den Eintrag eines bestimmten Users zurück
    """

    User = Query()
    return self.db.search(User.USER_ID == user_id)


def insert(self, user_id, name):
    """
    Diese Funktion fügt einen neuen Eintrag in die Datenbank ein
    Das Alter (Age) ist bisher nur ein Dummy.
    """

    self.db.insert({'USER_ID': user_id, 'USER': name, 'AGE': 10})


def remove_all(self):
    """
    Diese Funktion entfernt alle Einträge aus der Datenbank
    """
    self.db.purge()


def user_exists(self, user_id):
    """
    Diese Funktion prüft, ob ein User in der DB existiert
    und gibt als Ergebnis einen Bool zurück
    """

    User = Query()
    result = self.db.search(User.USER_ID == user_id)
    if result:
        return True
    return False

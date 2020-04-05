
from tinydb import TinyDB
DB_path = './../data/dummydb.json'

def push_data(doc):
    db = TinyDB(DB_path)
    db.insert(doc)


def get_all():
    db = TinyDB(DB_path)
    return str(db.all())
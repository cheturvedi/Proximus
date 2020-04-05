
from random import choice,randint
from string import ascii_uppercase,digits

from tinydb import TinyDB

DB_path = './data/dummydb.json'
timestamp = 1586005981

all_data = {}
for _ in range(0,randint(0,10)):
    random_time = timestamp + randint(-1000,1000)
    pos_users  = []
    for _ in range(0,randint(0,15)):
        user = ''.join([choice(ascii_uppercase+digits) for _ in range(16)])
        pos_users.append(user)
    all_data[random_time] = pos_users

db = TinyDB(DB_path)
db.insert(all_data)
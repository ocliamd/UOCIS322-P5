from pymongo import MongoClient
from db import Mongodb

def test_db():
    db.database.drop()
    db.database.insert({'BrevetDistance': 200, 'StartTime': "30:06"}) 
    print(list(db.database.find_one()))
    assert list(db.database.find_one()) == ['_id', 'BrevetDistance', 'StartTime']
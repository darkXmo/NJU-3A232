import pymongo
import random
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
import time

db = mongo_client['test']

def timedTask(db):
    while(True):
        types = db['types']
        types.delete_many({})
        type1 = {
            'distance' : round(random.random(),3)
        }
        type2 = {
            'distance' : round(random.random(),3)
        }
        type3 = {
            'distance' : round(random.random(),3)
        }
        type4 = {
            'distance' : round(random.random(),3)
        }
        type5 = {
            'distance' : round(random.random(),3)
        }
        types.insert_many([type1, type2, type3, type4, type5])



        countries = db['countries']
        countries.delete_many({})
        country1 = {
            'distance' : round(random.random(),3)
        }
        country2 = {
            'distance' : round(random.random(),3)
        }
        countries.insert_many([country1, country2])

        time.sleep(3)

timedTask(db);
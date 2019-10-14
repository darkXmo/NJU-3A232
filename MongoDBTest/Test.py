import pymongo
import random
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
import time

db = mongo_client['test']

def timedTask(db):
    while(True):
        types = db['types']
        results = types.find({})
        res = []
        for result in results:
            res.append(result)
        type1 = {
            'distance' : round(res[0]['distance']+(round(random.random(),3)-0.5)*0.02, 3)
        }
        type2 = {
            'distance' : round(res[1]['distance']+(round(random.random(),3)-0.5)*0.04, 3)
        }
        type3 = {
            'distance' : round(res[2]['distance']+(round(random.random(),3)-0.5)*0.02, 3)
        }
        type4 = {
            'distance' : round(res[3]['distance']+(round(random.random(),3)-0.5)*0.03, 3)
        }
        type5 = {
            'distance' : round(res[4]['distance']+(round(random.random(),3)-0.5)*0.03, 3)
        }
        types.delete_many({})
        types.insert_many([type1, type2, type3, type4, type5])



        countries = db['countries']
        results = countries.find({})
        res = []
        for result in results:
            res.append(result)
        
        country1 = {
            'distance' : round(res[0]['distance']+(round(random.random(),3)-0.5)*0.03, 3)
        }
        country2 = {
            'distance' : round(res[1]['distance']+(round(random.random(),3)-0.5)*0.03, 3)
        }
        countries.delete_many({})
        countries.insert_many([country1, country2])

        time.sleep(1)

timedTask(db)
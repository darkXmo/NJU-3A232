import pymongo
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

db = mongo_client['test']
print(db.collection_names())
countries = db['countries']
print(countries.find())
results = countries.find()
for result in results:
    print(result)

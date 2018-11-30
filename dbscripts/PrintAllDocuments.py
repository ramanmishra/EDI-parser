from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.makeathon
    collection = db['reports']
    cursor = collection.find()
    for document in cursor:
          print(document)
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.makeathon
    collection = db['template']
    cursor = collection.find({"name": "PurchaseOrder"}, {'_id': False})
    first = cursor
    for document in cursor:
        print(document)
        # print(document.get("templates")[0]["config"])
        # file_content = json.dumps(document, indent=4)
        # print(file_content)

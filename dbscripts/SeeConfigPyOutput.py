import json
from pymongo import MongoClient

client = MongoClient("localhost", 27017, maxPoolSize=50)
db = client.templates
collection = db['template']
cursor = collection.find({"name":"Agent1"})
for document in cursor:
    id = document.get("_id")
    file_content = json.dumps(document.get("templates").get("config_py"), indent=4)
    print(file_content)
from pymongo import MongoClient
import json

if __name__ == '__main__':
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.makeathon
    collection = db['agents']
    cursor = collection.find({"name": "HealthCare"}, {'_id': False})
    first = cursor
    for document in cursor:
        active_version = document.get("active_version")

        for i in document.get("templates"):
            if i.get("version") == active_version:
                print(i)

        file_content = json.dumps(document.get("templates")[0].get("config"), indent=4)
        delimiter_db = document.get("delimiter")
        content_separator = document.get("content_separator")
        output_format = document.get("output_format")
        # print(document.get("templates")[0]["config"])
        # file_content = json.dumps(document, indent=4)
        # print(file_content)

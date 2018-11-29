from pymongo import MongoClient

# read json from the db

client = MongoClient()
db = client.templates
post = {"name":"mukesh",
        "age":"24"}

#db.template.insert(post)
db.template.save(post)
#print("post_id is:: ", post_id)
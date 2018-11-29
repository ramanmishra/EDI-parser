# import json
# from pymongo import MongoClient
# import schedule
# import time
# # read json from the db
#
# def isNestedValue(file_content_line):
#     if "_" in file_content_line and ":" in file_content_line and "comment" not in file_content_line:
#         return True
#     else:
#         return False
#
# def getTupledValue(file_content_line):
#     value = file_content_line.split(":")
#     key = value[0].strip().replace("\"","").split("_")[0].strip()
#     return (int(key), value[1].strip().replace(",","").replace("\"",""))
#
# def job():
#     print("Job started!!!")
#     client = MongoClient("localhost", 27017, maxPoolSize=50)
#     db = client.templates
#     collection = db['template']
#     cursor = collection.find({"name":"Agent1"})
#     for document in cursor:
#         id = document.get("_id")
#         file_content = json.dumps(document.get("templates").get("config"), indent=4)
#         header_stack = []
#         file_content = file_content.split("\n")
#         result = "{"
#         contentCount = 0            #since we are ignoring content from beginning so need to remove them from the end tag too
#         dict = {}
#         idx = 1
#         while idx < len(file_content):
#             #for idx in range(1, len(file_content)):
#             bool = False            #if we are adding trailer there is no need to add file_content_line once again
#             file_content_line = file_content[idx].strip()
#             if file_content_line.startswith("\"delimiter"):
#                 result = result + file_content_line
#             elif file_content_line.startswith("\"header"):
#                 result = result + file_content_line.split(":")[0] + ": {\"before\" : "
#             elif file_content_line.startswith("\"content"):
#                 contentCount = contentCount + 1
#                 idx = idx + 1
#                 continue
#             elif file_content_line.startswith("\"_comment"):
#                 continue
#             elif file_content_line.startswith("\"title"):
#                 title = (file_content_line.split(":")[1]).strip().replace(",", "")
#                 result = result + title + "},"
#                 header_stack.append(title.replace("\"", ""))
#             else:
#                 if file_content_line.startswith("}"):
#                     if len(header_stack) > 0:
#                         top = header_stack.pop()
#                         if top != "i":
#                             index= len(header_stack) - header_stack.count("i")
#                             result = result + ",\"trailer_" + str(index) + "\" : { \"after\": \"/" + top + "\"},"
#                             bool = True
#                 elif ":" in file_content_line and (file_content_line.split(":")[1]).strip() == "{":
#                     header_stack.append("i")
#                 if bool==False:
#                     if isNestedValue(file_content_line):
#                         values = getTupledValue(file_content_line)
#                         dict[values[0]] = [values[1]]
#                         while isNestedValue(file_content[idx+1]) and getTupledValue(file_content[idx+1])[0]==values[0]:
#                             idx = idx + 1
#                             file_content_line = file_content[idx].strip()
#                             additionalValues = getTupledValue(file_content_line)
#                             dict[additionalValues[0]] += [additionalValues[1]]
#                         result = result + '"{}"'.format(values[0]) + ":" + json.dumps(dict[values[0]]) + ","
#                     else:
#                         result = result + file_content_line
#             idx = idx + 1
#
#         import ast
#
#         res = result[:-contentCount]
#         r = ast.literal_eval(res)
#         #file = open("output1.json", "w")
#         #file.write(result[:-contentCount])
#         collection.update({"_id": id},{"$set":{"templates.config_py":r}})
#
# schedule.every().hour.do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
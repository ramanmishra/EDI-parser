import json
from flask import Flask

# read json from the db

with open("C:/Users/Raman/Desktop/parser/a.json", "r") as ui_json:
    file_content = ui_json.read()
    backend = json.loads(file_content)
    header_stack = []
    file_content = file_content.split("\n")
    result = "{"

contentCount = 0  # since we are ignoring content from beginning so need to remove them from the end tag too
for idx in range(1, len(file_content)):
    bool = False  # if we are adding trailer there is no need to add file_content_line once again
    file_content_line = file_content[idx].strip()
    if file_content_line.startswith("\"delimiter"):
        result = result + file_content_line
    elif file_content_line.startswith("\"header"):
        result = result + file_content_line.split(":")[0] + ": {\"before\" : "
    elif file_content_line.startswith("\"content"):
        contentCount = contentCount + 1
        continue
    elif file_content_line.startswith("\"title"):
        title = (file_content_line.split(":")[1]).strip().replace(",", "")
        result = result + title + "},"
        header_stack.append(title.replace("\"", ""))
    else:
        if file_content_line.startswith("}"):
            if len(header_stack) > 0:
                top = header_stack.pop()
                if top != "i":
                    index = len(header_stack) - header_stack.count("i")
                    result = result + ",\"trailer_" + str(index) + "\" : { \"after\": \"/" + top + "\"},"
                    bool = True
        elif ":" in file_content_line and (file_content_line.split(":")[1]).strip() == "{":
            header_stack.append("i")
        if not bool:
            result = result + file_content_line

file = open("output.json", "w")
file.write(result[:-contentCount])

from pymongo import MongoClient
import json
import re
from os import listdir
from os.path import isfile, join


def get_header_or_trailer(header_trailer):
    return header_trailer[1][:-1].strip().replace("\'", "")


def get_template():
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.makeathon
    collection = db['templates']
    cursor = collection.find({"name": "Agent1"})
    for document in cursor:
        file_content = json.dumps(document.get("templates")[0].get("config"), indent=4)
        delimiter = document.get("delimiter")
        return (file_content, delimiter)


mypath = "../unprocessed_files"

template, delimiter = get_template()
fileNames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
template_map = json.loads(template)
number_of_failed_file = 0
for file in fileNames:
    outputXml = ""
    fields = []
    path = "C:/Users/raman.mishra/Desktop/parserBackend/EDI-parser/unprocessed_files/"
    after = ""

    with open(path + file) as f:
        is_processed = True
        text = f.read().replace("~", "")
        lines = text.split("\n")
        for line in lines:
            fields += [(line.split(delimiter))]
        nmc = 0
        ces_delimiter = str(fields[0][-1])
        is_end = True
        for field in fields:
            try:
                input_header = str(field[0]).lower()
                template_value = template_map[input_header]
                rowFields = json.loads(str(template_value).replace("\'", "\""))
                template_keys = list(template_map.keys())
                header_idx_value = str(template_keys[template_keys.index(input_header) - 1])
                trailer_idx_value_f = str(template_keys[template_keys.index(input_header) + 1])
                trailer_idx_value_p = str(template_keys[template_keys.index(input_header) - 1])

                if re.match("header_", header_idx_value):
                    header_value = str(template_map[header_idx_value]).split(":")
                    header = get_header_or_trailer(header_value)
                    outputXml += "<" + header + ">" + "\n"
                    is_end = True

                if re.match("trailer_", trailer_idx_value_p) and is_end:
                    trailer_value_p = str(template_map[trailer_idx_value_p]).split(":")
                    trailer_p = get_header_or_trailer(trailer_value_p)
                    outputXml += "<" + trailer_p + ">" + "\n"
                    is_end = False

                if re.match("trailer_", trailer_idx_value_f) and not is_end and template_keys.index(
                        input_header) != len(template_map) - 2:
                    trailer_value_f = str(template_map[trailer_idx_value_f]).split(":")
                    trailer_f = get_header_or_trailer(trailer_value_f)
                    outputXml += "<" + trailer_f + ">" + "\n"
                else:
                    trailer_value_f = str(template_map[trailer_idx_value_f]).split(":")
                    trailer_f = get_header_or_trailer(trailer_value_f)
                    after = "<" + trailer_f + ">"

                for rowK, rowV in rowFields.items():
                    if str(rowK).isdigit() and len(re.split(r",", str(rowV))) > 1 or \
                            len(re.split(ces_delimiter, str(rowV))) > 1:
                        lenOfPossibleValues = nmc % len(rowV)
                        if (len(str(rowV).split(ces_delimiter))) > 1:
                            ces_value = list(
                                zip(list(field[int(rowK)].split(ces_delimiter)),
                                    str(rowV).split(ces_delimiter)))
                            for elem in ces_value:
                                outputXml += "<" + elem[1].strip() + ">" + elem[0] + "</" + elem[
                                    1].strip() + ">\n"
                        else:
                            outputXml += "<" + list(rowV)[lenOfPossibleValues] + ">" + field[int(rowK)] \
                                         + "</" + list(rowV)[lenOfPossibleValues] + ">\n"
                        nmc += 1
                    else:
                        if str(rowK).isdigit():
                            keyNumber = int(str(rowK))
                            valueIdx = 0
                            if keyNumber >= len(field):
                                valueIdx = keyNumber % len(field)
                            else:
                                valueIdx = int(rowK)
                            outputXml += "<" + rowFields[rowK] + ">" + field[valueIdx] + "</" + rowFields[rowK] + ">\n"

            except Exception as e:
                is_processed = False
                number_of_failed_file += 1
                failed_file = open("C:/Users/raman.mishra/Desktop/parserBackend/EDI-parser/failed_files/" + file, "w")
                msg = "file unprocessed : {}".format(file)
                failed_file.write(str(msg))

        outputXml += after
        if is_processed:
            output_file = open(
                "C:/Users/raman.mishra/Desktop/parserBackend/EDI-parser/processed_files/" + file.replace(".txt",
                                                                                                         "") + ".xml",
                "w")
            output_file.write(outputXml)
        print("file Processed {}".format(file))
print("number of failed files : {}".format(number_of_failed_file))

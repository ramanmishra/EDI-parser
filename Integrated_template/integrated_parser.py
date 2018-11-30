import json
import time
import re
from os import listdir
from os.path import isfile, join
from pymongo import MongoClient
import schedule

client = MongoClient("localhost", 27017, maxPoolSize=50)
db = client.makeathon

def get_header_or_trailer(header_trailer):
    return header_trailer[1][:-1].strip().replace("\'", "")


def get_template(template_name):
    collection = db['agents']
    cursor = collection.find({"name": template_name})
    file_content = ""
    delimiter_db = ""
    content_separator = ""
    output_format = ""
    agent = ""
    for document in cursor:
        active_version = document.get("active_version")

        for template_itr in document.get("templates"):
            if template_itr.get("version") == active_version:
                file_content = json.dumps(template_itr.get("config"), indent=4)
                delimiter_db = document.get("delimiter")
                content_separator = document.get("content_separator")
                output_format = document.get("output_format")
                agent = document.get("name")
                active_template = document.get("active_template")
    return (file_content, delimiter_db, content_separator, output_format, agent, active_template)


def get_header_or_trailer(header_trailer):
    return header_trailer[1][:-1].strip().replace("\'", "")


def start_parser():
    status_table = {"agent": '', "template": '', "filename": '', "status": '', "failurereason": ''}
    mypath = "../unprocessed_files/"
    fileNames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    number_of_failed_file = 0
    for file in fileNames:
        file_name = file
        template, delimiter, content_sep, format_output, agent, active_template = get_template(file_name.split("_")[0])
        template_map = json.loads(template)
        outputXml = ""
        fields = []
        path = "C:/Users/raman.mishra/Desktop/parserBackend/EDI-parser/unprocessed_files/"
        after = ""

        with open(path + file) as f:
            text = f.read().replace("~", "")
            lines = text.split("\n")
            for line in lines:
                fields += [(line.split(delimiter))]
            nmc = 0
            ces_delimiter = content_sep
            is_end = True
            is_processed = True
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
                                    if elem[1] != " ":
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
                                outputXml += "<" + rowFields[rowK] + ">" + field[valueIdx] + "</" + rowFields[
                                    rowK] + ">\n"

                except Exception as e:
                    is_processed = False
                    failed_file = open("C:/Users/raman.mishra/Desktop/parserBackend/EDI-parser/failed_files/" + file,
                                       "w")
                    msg = "file unprocessed : {}".format(file)
                    failed_file.write(str(msg))

            outputXml += after
            output_file = open(
                "C:/Users/raman.mishra/Desktop/parserBackend/EDI-parser/processed_files/" + file_name.split("_")[
                    0] + "/" +
                file.replace(".txt", "") + ".xml", "w")
            status_table = {"agent": agent, "template": active_template, "filename": file, "status": is_processed,
                            "failurereason": ''}
            report_db = db['reports']
            report_db.save(status_table)
            output_file.write(outputXml)
            print(output_file.name)
            # convertor = xml2csv(output_file.name, "xyz.csv", )
            # convertor.convert(tag="item")

            print("file Processed {}".format(file))
    print("number of failed files : {}".format(number_of_failed_file))


def job():
    start_parser()


schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()

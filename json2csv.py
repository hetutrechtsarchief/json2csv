#!/usr/bin/env python3


import json,csv,sys,glob
from sys import argv

# findList: searches in an JSON blob for the first 'list'. This can be the root object or any of the childs that is a list.
def findList(data): 
    if type(data)==list: # if the root item is a list
        items = data
    else: # if not, find the first item under the root item that is a list
        for obj in data.values():
            if type(obj)==list:
                items = obj
    return items if items else None

# search through all items to find all key names
def getAllKeys(items):
    keys = []
    for item in items:
        for key,value in item.items():
            if not key in keys:
                keys.append(key)
    return keys

##########################################
# main

if len(argv)!=3:
  print("Usage: json2csv {INPUT_JSON} {OUTPUT_CSV}")
  sys.exit()

input_filename = argv[1]
output_filename = argv[2]

header = None
# output_filename = "result.csv"


# for filename in argv[1:]:
with open(input_filename, encoding="utf-8") as json_file:
    data = json.load(json_file)

    items = findList(data)

    if not type(items)==list:
        print("Error: could not find a 'list' in ",filename)
        sys.exit(1)

    if not header:
        header = getAllKeys(items) # header is created based on just the first json file.
        writer = csv.DictWriter(open(output_filename,"w",encoding="utf-8"), fieldnames=header, delimiter=';', quoting=csv.QUOTE_ALL, dialect='excel')
        # open(output_filename,"w", encoding="utf-8")
        writer.writeheader()

    writer.writerows(items)








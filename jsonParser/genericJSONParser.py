#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2016 Anshul Joshi anshuljoshi.cse@gmail.com
# license: GNU GENERAL PUBLIC LICENSE <http://www.gnu.org/licenses/gpl-3.0.html>
#
# Anshul Joshi anshuljoshi.github.io

########################## GENERIC JSON PARSER ##############################

# json (serialized or deserialized)
# key : key whose value is required
# superkey : (optional) If key is ambiguous
# lvl : (optional) used only if superkey is present
# specifies the location for key in list of json

#example:
# {"name": "sample", "def": [{"hello": 1,"world":
#                                    [{"name": "ABC","type": "STRING"},
#                                            {"name": "XYZ","type": "STRING"}]}]}

# To get name:ABC,  genericJSONParser(example_json, 'name', 'world')
# To get name:sample,  genericJSONParser(example_json,'name')

############################################################################

import json, sys

def jsonisdict(myjson, key, superkey=0, lvl=0):
    for jsonkey in myjson:
        if type(myjson[jsonkey]) in (list, dict):
            return genericJSONParser(myjson[jsonkey], key)
        elif jsonkey == key:
            return myjson[jsonkey]

def jsonislist(myjson, key, superkey=0, lvl=0):
    for item in myjson:
        if type(item) in (list, dict):
            return genericJSONParser(item, key)

def superkeyjson(myjson, key, superkey, lvl=0):
    if type(myjson) is dict:
        for skey in myjson:
            if skey == superkey and type(myjson[skey]) == list:
                return genericJSONParser(myjson[skey][lvl],key)
            elif skey == superkey:
                return genericJSONParser(myjson[skey],key)
            elif type(myjson[skey]) in (list, dict):
                return genericJSONParser(myjson[skey], key, superkey, lvl)
    elif type(myjson) is list:
        return jsonislist(myjson, key, superkey, lvl=0)

def genericJSONParser(myjson, key, superkey=0, lvl=0):
    if type(myjson) == str:
        myjson = json.loads(myjson)
    if superkey!=0:
        return superkeyjson(myjson, key, superkey, lvl=0)
    elif type(myjson) is dict:
        return jsonisdict(myjson, key, superkey=0, lvl=0)
    elif type(myjson) is list:
        return jsonislist(myjson, key, superkey=0, lvl=0)

def main():
    try:
        myjson = raw_input("Enter json: ")
        key = raw_input("Enter key: ")
        superkey = raw_input("Enter superkey (enter 0 if not needed): ")
        lvl = raw_input("Enter level (enter 0 if not using superkey): ")
        if superkey=='0':
            superkey=int(superkey)
            lvl = int(lvl)
        print genericJSONParser(myjson, key, superkey, lvl)
    except:
        print 'Try Again with valid inputs'

if __name__ == '__main__':
    print "USAGE: python genericJSONParser.py json key <optional>superkey(if any) <optional>level-of-key-in-superkey(if any)"
    main()

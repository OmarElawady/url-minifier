import json
from flask import request
from os.path import exists

def convert_char(num):
    if num < 10:
        print(ord('0') + num)
        return chr(ord('0') + num)
    elif num < 10 + 26:
        return chr(num - 10 + ord('a'))
    else:
        return chr(num - 10 - 26 + ord('A'))
def convert_num(num):
    string = ""
    base = 10 + 26 + 26
    while num:
        string += convert_char(num % base)
        num = num // base
    return string

def create_if_doesnt_exist():
    if not exists('minifier/data.json'):
        fd = open('minifier/data.json', 'w+')
        fd.write('{}')
        fd.close()

def get_data():
    create_if_doesnt_exist()
    with open('minifier/data.json', 'r') as fd:
        return json.loads(fd.read())

def set_data(d):
    with open('minifier/data.json', 'w') as fd:
        fd.write(json.dumps(d))
    

def shortify(link):
    d = get_data()
    shortened = convert_num(len(d) + 1)
    new_link = 'http://' + request.host + '/' + shortened
    d[shortened] = link
    set_data(d)
    return new_link

def get_link(shorted):
    return get_data()[shorted]



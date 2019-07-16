import json
from flask import request
from os.path import exists
data = {}
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

def shortify(link):
    shortened = convert_num(len(data) + 1)
    new_link = 'http://' + request.host + '/' + shortened
    data[shortened] = link
    return new_link

def get_link(shorted):
    if shorted in data:
        return data[shorted]
    else:
        return None



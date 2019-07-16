import redis
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

def shortify(link):
    r = redis.Redis()
    shortened = convert_num(r.hlen('links') + 1)
    new_link = 'http://127.0.0.1:5000/' + shortened
    r.hset('links', shortened, link)
    return new_link

def get_link(shorted):
    r = redis.Redis()
    return r.hget('links', shorted)


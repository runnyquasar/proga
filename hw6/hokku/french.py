import random


def word(name):
    name = name + '.txt'
    with open('/Users/andreakimov/Desktop/hokku/' + name, encoding='utf-8') as f:
        part = f.read()
        part = part.replace('\uffef', '')
        part = part.split('|')
        part = random.choice(part)
        return part


def short_sent():
    n = random.random()
    if n < 1:
        short = word('nom2') + word('verb3') + word('punc')
    else:
        short = word('nom3') + word('verb2') + word('punc')
    return short


def long_sent():
    n = random.random()
    if n < 0.5:
        long = word('exc') + short_sent()
    elif 1 >= n >= 0.5:
        long = word('nom2') + word('no') + word('verb3') + word('pas') + word('punc')
    elif 10 >= n > 1:
        long = word('time') + short_sent()
    else:
        long = word('nom3') + word('no') + word('verb2') + word('pas') + word('punc')
    return long


def make_verse():
    print(short_sent())
    print(long_sent())
    print(short_sent())


make_verse()

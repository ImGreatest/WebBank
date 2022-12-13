import datetime
import random


def define(list_answers=list, element=str) -> str:
    return list_answers[int(element)-1]

def fullname_share(element=str) -> list:
    element += ' '
    names, word = [], ''
    for i in element:
        if i == ' ':
            names.append(word)
            word = ''
        else:
            word += i

    return names

def generate_code_card() -> str:
    pass

def generate_pulldate() -> str:
    month = str(random.randint(1, 12))
    if len(month) == 1:
        month = '0' + month
    now = datetime.datetime.now()
    year = now.year + 10
    return month + '/' + str(year)

def generate_cvv()-> str:
    numeric = str(random.randint(000, 999))
    if len(numeric) == 2:
        return '0' + numeric
    elif len(numeric) == 1:
        return '00' + numeric


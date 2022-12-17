import datetime
import random
import re

from sql_requests import *


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

def luhn(cardnumber=str) -> bool:
    sum = 0
    for i in cardnumber:
        if cardnumber.index(i) % 2 == 0:
            buff = int(i) * 2
            if buff > 9:
                buff -= 9
            sum += buff
        else:
            sum += int(i)

    return sum % 10 == 0

def generate_code_card(payment_system=str) -> str:
    code_bank, code_program = '53791', '01'
    if payment_system == 'Мир':
        first = '2'
    elif payment_system == 'American Express':
        first = '3'
    elif payment_system == 'Visa':
        first = '4'
    elif payment_system == 'MasterCard':
        fisrt = '5'
    elif payment_system == 'Maestro':
        first = random.choice(3, 5, 6)
    elif payment_system == 'China UnionPay':
        first = '6'
    elif payment_system == 'УЭК':
        first = '7'

    trust = False
    while not trust:
        cardnumber = first + '53791' + '01' + str(random.randint(1000, 9999)) + str(random.randint(1000, 9999))
        if luhn(cardnumber):
            trust = True

    cardnumber = re.sub(r'.{4}', r'\g<0> ', cardnumber)

    return cardnumber


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

    else:
        return numeric


def nowdate()->str:
    now = datetime.datetime.now()

    return str(now.date())


def percent_deposit(term=int) -> str:
    if 3 <= term >= 5:
        return '6'
    elif 6 <= term >= 12:
        return '7'
    elif 13 <= term >= 18:
        return '7.5'
    elif 19 <= term >= 25:
        return '8'
    elif 26 <= term >= 32:
        return '8.5'
    else:
        return '9'

import datetime

import django.contrib.auth
import django.contrib.auth.forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from sql_requests import *
from func import *
from  django.contrib.auth.models import User

def index(request):
    customers = SQLRequests(table='customers').SelectRequest(specify=None)
    return render(request, 'djangoWebbank/home.html', {'customers': customers})

def create(request):
    customers = SQLRequests(table='customers').SelectRequest(specify=None)
    if request.method == "POST":
        form = CustomerPostFrom(request.POST)
        if form.is_valid():

            id = SQLRequests(table='customers').CountIdReq() + 1
            if len(form.cleaned_data.get('fullname')) > 10 and ' ' in form.cleaned_data.get('fullname'):
                fullname = fullname_share(form.cleaned_data.get('fullname'))
                firstname, secondname, thirdname = fullname[0], fullname[1], fullname[-1]
                fullname = form.cleaned_data.get('fullname')
            else:
                fullname = form.cleaned_data.get('fullname')

            birthday = form.cleaned_data.get('birthday')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            payment_system = define(['Visa', 'MasterCard', 'Мир', 'American Express', 'Maestro', 'China UnionPay', 'УЭК'], form.cleaned_data.get('payment_system'))
            currency = define(['rub', 'euro', 'dollar'], form.cleaned_data.get('currency'))
            code = form.cleaned_data.get('secret_code')
            passport = str(form.cleaned_data.get('passport')).replace(' ', '')

            code_card = generate_code_card(payment_system)

            id_customer = SQLRequests(table='customers').CountIdReq() + 1
            amount = 0
            type = 'Defoult'
            pulldate = generate_pulldate()
            cvv = generate_cvv()

            if 'createb' in request.POST:
                User.objects.create_user(username=fullname, email=email, password=code)
                createNewCustomer(id, firstname, secondname, thirdname, birthday, phone, email, currency, code, passport)
                createNewAccount(code_card, id_customer, amount, type, pulldate, cvv)

            return redirect('/')

    else:
        form = CustomerPostFrom()

    return render(request, 'djangoWebbank/home.html', {'form': form,  'customers': customers})


def mortgage(request):
    if request.method == 'POST':
        form = MortgagePostForm(request.POST)
        if form.is_valid():

            id = SQLRequests(table='customers').CountIdReq() + 1
            id_mort = SQLRequests(table='mortgage').CountIdReq() + 1
            id_customer = SQLRequests(table='customers').CountIdReq() + 1

            if len(form.cleaned_data.get('fullname')) > 10 and ' ' in form.cleaned_data.get('fullname'):
                fullname = fullname_share(form.cleaned_data.get('fullname'))
                firstname, secondname, thirdname = fullname[0], fullname[1], fullname[-1]
                fullname = form.cleaned_data.get('fullname')
            else:
                fullname = form.cleaned_data.get('fullname')

            cost = form.cleaned_data.get('cost')
            contribution = form.cleaned_data.get('contribution')
            term = form.cleaned_data.get('term')

            date_take = datetime.datetime.now().date()
            date_retrieve = date_take + datetime.timedelta(weeks=int(term)*48)

            phone = form.cleaned_data.get('phone')
            birthday = form.cleaned_data.get('birthday')
            passport = form.cleaned_data.get('passport')
            email = form.cleaned_data.get('email')

            currency = 'rub'
            code = 'None'

            if 'next_mortgage' in request.POST:

                createNewCustomer(id, firstname, secondname, thirdname, birthday, phone, email, currency, code, passport)
                createNewMotgage(str(id_mort), str(id_customer), str(cost), str(date_take), str(date_retrieve), str(term), str(contribution))

            return redirect('/')

    else:
        form = MortgagePostForm()

    return render(request, 'djangoWebbank/mortgage.html', {'form': form})


def credit(request):
    if request.method == 'POST':
        form = CreditForm(request.POST)

        if form.is_valid():

            amount = form.cleaned_data.get('amount')
            term = form.cleaned_data.get('term')
            target = define(["Ремонт", "Покупка недвижимости", "Покупка авто", "Погашение кредита", "Развитие бизнеса", "Лечение", "Путешествие", "Иное"], form.cleaned_data.get('target'))
            personal_revenue = form.cleaned_data.get('personal_revenue')
            education = define(["Начальное, среднее", "Неполное высшее", "Высшее", "Второе высшее", "Ученая Степень"], form.cleaned_data.get('education'))
            family_status = define(["Холост/не замужем", "Разведен(а)", "Гражданский брак", "Женат/замужем", "Вдовец/вдова"], form.cleaned_data.get('family_status'))
            foreign_passport = form.cleaned_data.get('foreign_passport')
            car = define(["Нет", "Отечественный", "Инномарка"], form.cleaned_data.get('car'))
            pledge = define(["Нет", "Авто", "Недвижимость"], form.cleaned_data.get('pledge'))

            date_take = datetime.datetime.now().date()
            date_retrieve = date_take + datetime.timedelta(weeks=int(term)*48)

            id = SQLRequests(table='customers').CountIdReq() + 1
            id_cre = SQLRequests(table='credits').CountIdReq() + 1
            id_inf = SQLRequests(table='credit_information').CountIdReq() + 1
            id_customer = SQLRequests(table='customers').CountIdReq() + 1
            if len(form.cleaned_data.get('fullname')) > 10 and ' ' in form.cleaned_data.get('fullname'):
                fullname = fullname_share(form.cleaned_data.get('fullname'))
                firstname, secondname, thirdname = fullname[0], fullname[1], fullname[-1]
                fullname = form.cleaned_data.get('fullname')
            else:
                fullname = form.cleaned_data.get('fullname')
            birthday = form.cleaned_data.get('birthday')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            currency = 'rub'
            code = 'None'
            passport = form.cleaned_data.get('passport')

            if 'next_credit' in request.POST:

                createNewCustomer(id, firstname, secondname, thirdname, birthday, phone, email, currency, code, passport)
                createNewCredit(id_cre, id_customer, amount, date_take, date_retrieve, target)
                createNewCreditInformation(id_inf, id_customer, personal_revenue, education, family_status, foreign_passport, car, pledge)

                return redirect('/')

    else:
        form = CreditForm()

    return render(request, 'djangoWebbank/credit.html', {'form': form})

def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)

        if form.is_valid():

            deposit = form.cleaned_data.get('deposit')
            term = form.cleaned_data.get('term')
            currency = define(['rub', 'euro', 'dollar'], form.cleaned_data.get('currency'))
            percents_on_account = form.cleaned_data.get('percents_on_account')
            rate = percent_deposit(int(term))

            id = SQLRequests(table='customers').CountIdReq() + 1
            id_customer = id
            id_dep = SQLRequests(table='deposits').CountIdReq() + 1

            if len(form.cleaned_data.get('fullname')) > 10 and ' ' in form.cleaned_data.get('fullname'):
                fullname = fullname_share(form.cleaned_data.get('fullname'))
                firstname, secondname, thirdname = fullname[0], fullname[1], fullname[-1]
                fullname = form.cleaned_data.get('fullname')
            else:
                fullname = form.cleaned_data.get('fullname')

            birthday = form.cleaned_data.get('birthday')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            passport = form.cleaned_data.get('passport')
            date_open = datetime.datetime.now().date()
            code = 'None'


            if 'Depb' in request.POST:
                createNewCustomer(id, firstname, secondname, thirdname, birthday, phone, email, currency, code, passport)
                createNewDeposit(id_dep, id_customer, currency, deposit, date_open, term, rate, percents_on_account)

            return redirect('/')

    else:
        form = DepositForm()

    return render(request, 'djangoWebbank/deposit.html', {'form': form})

def profileUserHome(request, user):

    return render(request, 'djangoWebbank/profile_home.html')

def profileUserCredits(request, user):

    return render(request, 'djangoWebbank/profile_credits.html')

def profileUserMortgage(request, user):

    return render(request, 'djangoWebbank/profile_mortgage.html')

def profileUserDeposits(request, user):

    return render(request, 'djangoWebbank/profile_deposit.html')

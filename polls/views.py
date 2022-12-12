from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from sql_requests import *
from func import *


def index(request):
    customers = SQLRequests(table='customers').SelectRequest(specify=None)
    return render(request, 'djangoWebbank/home.html', {'customers': customers})

def create(request):
    customers = SQLRequests(table='customers').SelectRequest(specify=None)
    if request.method == "POST":
        form = CustomerPostFrom(request.POST)
        if form.is_valid():
            id = SQLRequests(table='customers').CountIdReq() + 1
            fullname = fullname_share(form.cleaned_data.get('fullname'))
            firstname, secondname, thirdname = fullname[0], fullname[1], fullname[-1]
            birthday = form.cleaned_data.get('birthday')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            currency = define(3, ['rub', 'euro', 'dollar'], form.cleaned_data.get('currency'))
            code = form.cleaned_data.get('secret_code')

            if 'createb' in request.POST:

                conn = db_conn()
                cur = conn.cursor()
                cur.execute('INSERT INTO customers(id, firstname, secondname, thirdname, birthday, phone, email, currency, code)' 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, firstname, secondname, thirdname, birthday, phone, email, currency, code))
                conn.commit()
                cur.close()
                conn.close()

            return redirect('/')

    else:
        form = CustomerPostFrom()

    return render(request, 'djangoWebbank/home.html', {'form': form,  'customers': customers})


def mortgage(request):
    if request.method == 'POST':
        form = MortgagePostForm(request.POST)
        form_contact_information = ContactInformationMortgageForm(request.POST)
        if form.is_valid():
            cost = form.cleaned_data.get('cost')
            contribution = form.cleaned_data.get('contribution')
            term = form.cleaned_data.get('term')

            if 'next_mortgage' in request.POST:
                pass


        if form_contact_information.is_valid():
            fullname = form_contact_information.cleaned_data.get('fullname')
            phone = form_contact_information.cleaned_data.get('phone')
            birthday = form_contact_information.cleaned_data.get('birthday')

            if 'next_mortgage' in request.POST:
                form = None
                form_contact_information = PassportInformationMortgageForm(request.POST)

            #return render('')


    else:
        form = MortgagePostForm()
        form_contact_information = ContactInformationMortgageForm()

    return render(request, 'djangoWebbank/mortgage.html', {'form': form, 'information_form': form_contact_information})


def credit(request):
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            target = define(8, ['Ремонт', 'Покупка недвижимости', 'Покупка авто', 'Погашение кредита', "Развитие бизнес", "Лечение", "Путешествие", "Иное"], form.cleaned_data.get('target'))
            fullname = fullname_share(form.cleaned_data.get('fullname'))
            firstname, secondname, thirdname = fullname[0], fullname[1], fullname[-1]
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')

            if 'next_credit' is request.POST:
                form = CreditFormPartTwo(request.POST)
                if form.is_valid():
                    serial_passport = form.cleaned_data.get('serial_passport')
                    number_passport = form.cleaned_data.get('number_passport')
                    birthday_place = form.cleaned_data.get('birthday_place')
                    code_place = form.cleaned_data.get('code_place')
                    code_give_passport = form.cleaned_data.get('code_give_passport')
                    address = form.cleaned_data.get('address')
                    is_liveplace = form.cleaned_data.get('address_is_liveplace')
                    additional_phone = form.cleaned_data.get('additional_phone')

                    if 'next_credit' is request.POST:
                        form = CreditFormPartThree(request.POST)
                        if form.is_valid():
                            type_employment = define(3, ['По найму', 'На себя', 'Не работаю'], form.cleaned_data.get('type_employment'))
                            name_company = form.cleaned_data.get('name_company')
                            post_job = form.cleaned_data.get('post_job')
                            experience = define(5, ['6 и менее месяцев', '0.5-3 года', '3-5 лет', '5-7 лет', '7 и более лет'], form.cleaned_data.get('experience'))

                            if 'next_credit' is request.POST:
                                form = CreditFormPartFour(request.POST)
                                if form.is_valid():
                                    personal_revenue = form.cleaned_data.get('personal_revenue')
                                    education = form.cleaned_data.get('education')
                                    family_status = define(5, ["Холост/не замужем", "Развен(а)", "Гражданский брак", "Женат/замужем", "Вдовец/вдова"], form.cleaned_data.get('family_status'))
                                    foreign_passport = form.cleaned_data.get('foreign_passport')
                                    car = define(3, ["Нет", "Отечественный", "Иннормарка"], form.cleaned_data.get('car'))
                                    pledge = define(3, ["Нет", "Авто", "Недвижимость"], form.cleaned_data.get('pledge'))

                                return render('/')

                            else:
                                form = CreditFormPartFour()
                    else:
                        form = CreditFormPartThree()
            else:
                form = CreditFormPartTwo()
    else:
        form = CreditForm()

    return render(request, 'djangoWebbank/credit.html', {'form': form})


def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        form_contact = DepositContactForm(request.POST)
        if form.is_valid() and form_contact.is_valid():
            term = form.cleaned_data.get('term')
            fullname = form_contact.cleaned_data.get('fullname')
            phone = form_contact.cleaned_data.get('phone')
            birthday = form_contact.cleaned_data.get('phone')
            email = form_contact.cleaned_data.get('email')
            account_check = form_contact.cleaned_data.get('account_check')

            if 'depositb' in request.POST:
                pass

            #return render('/')

    else:
        form = DepositForm()
        form_contact = DepositContactForm()

    return render(request, 'djangoWebbank/deposit.html', {'form': form,'form_contact': form_contact})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            secret_code = form.cleaned_data.get('secret_code')
            print(phone, secret_code)

            if 'login' in request.POST:
                pass

            return render('/')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

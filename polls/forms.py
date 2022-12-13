from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django_countries.fields import CountryField

#class LoginForm(forms.Form):
#    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
#    phone = forms.CharField(label='Введите телефон', validators=[phoneRegex], max_length=12, widget=forms.TextInput(attrs={"placeholder": "+7 923 456 7890"}))
#    secret_code = forms.CharField(label='Cекретный код', max_length=4, min_length=4, widget=forms.PasswordInput)

class CustomerPostFrom(forms.Form):
    fullname = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={"placeholder": "Ivanov Ivan Ivanovich"}), max_length=150)
    birthday = forms.DateField(label='Дата Рождения', widget=forms.SelectDateWidget(empty_label=(("Choose Month", "Choose Day", "Choose Year")), years=range(1934, 2005)))
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = forms.CharField(label="Телефон", validators=[phoneRegex], max_length=12, widget=forms.TextInput(attrs={"placeholder": "+7 923 456 7890"}), min_length=12)
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "IvanIvanov@domain.ru"}), max_length=150)
    payment_system = forms.TypedChoiceField(label="Платежная система", choices=((1, "Visa"), (2, 'MasterCard'), (3, 'Мир'), (4, 'American Express'), (5, 'Maestro'), (6, 'China UnionPay'), (7, 'УЭК')))
    currency = forms.TypedChoiceField(label="Валюта", choices=((1, 'Рубли'), (2, 'Евро'), (3, 'Доллар')))
    secret_code = forms.CharField(label='Секретный код', max_length=4, min_length=4, widget=forms.PasswordInput)

class MortgagePostForm(forms.Form):
    cost = forms.IntegerField(label="Цена недвижимости, ₽", max_value=1000000000, widget=forms.TextInput(attrs={"placeholder": "3 500 000"}))
    contribution = forms.IntegerField(label="Первоначальный взнос, ₽", max_value=100000000, widget=forms.TextInput(attrs={"placeholder":"700 000"}))
    term = forms.IntegerField(label="Срок кредита, лет", max_value=25, min_value=1, widget=forms.TextInput(attrs={"placeholder": "25"}))

class ContactInformationMortgageForm(forms.Form):
    fullname = forms.CharField(label="ФИО", max_length=50, widget=forms.TextInput(attrs={"placeholder": "Ivanov Ivan Ivanovich"}))
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = forms.CharField(label="Телефон", validators=[phoneRegex], max_length=12, min_length=12, widget=forms.TextInput(attrs={"placeholder": "+7 923 456 7890"}))
    birthday = forms.DateField(label="Дата рождения", widget=forms.SelectDateWidget(years=range(1924, 2005)))

class PassportInformationMortgageForm(forms.Form):
    serial_passport = forms.IntegerField(label='Серия паспорта', max_value=9999, min_value=1000, widget=forms.TextInput(attrs={"placeholder": "Серия паспорта*"}))
    number_passport = forms.IntegerField(label='Номер паспорта', max_value=999999, min_value=100000, widget=forms.TextInput(attrs={"placeholder": "Номер паспорта*"}))
    birthday_place = forms.CharField(label='Место рождения', max_length=100, min_length=10, widget=forms.TextInput(attrs={"placeholder": "Место рождения*"}))
    code_place = forms.IntegerField(label='Код подразделения', max_value=999999, min_value=100000, widget=forms.TextInput(attrs={"placeholder": "Код подразделения*"}))
    code_give_passport = forms.CharField(label="Кем выдан", min_length=25, widget=forms.TextInput(attrs={"placeholder": "Кем выдан*"}))
    address = forms.CharField(label="Адресс регистрации", min_length=10, widget=forms.TextInput(attrs={"placeholder": "Адрес регистрации*"}))
    address_is_liveplace = forms.BooleanField(label="Адрес проживания совпадает с адресом регистрации", required=False)

class DepositForm(forms.Form):
    deposit = forms.IntegerField(label='Размер вклада', min_value=25000, max_value=100000000, widget=forms.TextInput(attrs={"placeholder": "25000"}))
    term = forms.IntegerField(label='Срок вклада, мес.',min_value=3, max_value=36, widget=forms.TextInput(attrs={"placeholder": "3"}))

class DepositContactForm(forms.Form):
    fullname = forms.CharField(label='ФИО', max_length=50, widget=forms.TextInput(attrs={"placeholder": "Ivanov Ivan Ivanovich"}))
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = forms.CharField(label='Телефон', validators=[phoneRegex], max_length=12, widget=forms.TextInput(attrs={"placeholder": "+7 923 456 7890"}))
    birthday = forms.DateField(label='Дата Рождения', widget=forms.SelectDateWidget(years=range(1924, 2005)))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"placeholder": "IvanIvanov@domain.ru"}))
    account_check = forms.BooleanField(label='Есть счет в MamontBank', required=False)
    percents_on_account = forms.BooleanField(label='Зачислять процент на счет', required=False)

class CreditForm(forms.Form):
    target = forms.TypedChoiceField(label='Цель кредита', choices=((1, 'Ремонт'), (2, 'Покупка недвижимости'), (3, 'Покупка авто'), (4, 'Погашение кредита'), (5, 'Развитие бизнеса'), (6, 'Лечение'), (7, 'Путешествие'), (8,'Иное')))
    fullname = forms.CharField(label='ФИО', max_length=50, widget=forms.TextInput(attrs={"placeholder": "Ivanov Ivan Ivanovich"}))
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = forms.CharField(label='Телефон', validators=[phoneRegex], max_length=12, widget=forms.TextInput(attrs={"placeholder": "+7 923 456 7890"}), min_length=12)
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"placeholder": "IvanIvanov@domain.ru"}))

class CreditFormPartTwo(forms.Form):
    serial_passport = forms.IntegerField(label='Серия паспорта', max_value=9999, min_value=1000, widget=forms.TextInput(attrs={"placeholder": "Серия паспорта*"}))
    number_passport = forms.IntegerField(label='Номер паспорта', max_value=999999, min_value=100000, widget=forms.TextInput(attrs={"placeholder": "Номер паспорта*"}))
    birthday_place = forms.CharField(label='Место рождения', max_length=100, min_length=10, widget=forms.TextInput(attrs={"placeholder": "Место рождения*"}))
    code_place = forms.IntegerField(label='Код подразделения', max_value=999999, min_value=100000, widget=forms.TextInput(attrs={"placeholder": "Код подразделения*"}))
    code_give_passport = forms.CharField(label="Кем выдан", min_length=25, widget=forms.TextInput(attrs={"placeholder": "Кем выдан*"}))
    address = forms.CharField(label="Адресс регистрации", min_length=10, widget=forms.TextInput(attrs={"placeholder": "Адрес регистрации*"}))
    address_is_liveplace = forms.BooleanField(label="Адрес проживания совпадает с адресом регистрации", required=False)
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    additionally_phone = forms.CharField(label='Дополнительный телефон', validators=[phoneRegex], max_length=12, widget=forms.TextInput(attrs={"placeholder": "+7 923 456 7890"}), required=False)

class CreditFormPartThree(forms.Form):
    type_employment = forms.TypedChoiceField(label="Тип занятости", choices=((1, 'По найму'), (2, "На себя"), (3, "Не работаю")))
    name_company = forms.CharField(label='Название компании', min_length=8, widget=forms.TextInput(attrs={"placeholder": "ООО Компания*"}))
    post_job = forms.CharField(label='Название должности', min_length=3, widget=forms.TextInput(attrs={"placeholder": "Менеджер*"}))
    experience = forms.TypedChoiceField(label='Стаж в организации', choices=((1, '6 и менее месяцев'), (2, "0.5-3 года"), (3, "3-5 лет"), (4, "5-7 лет"), (5, "7 и более лет")))

class CreditFormPartFour(forms.Form):
    personal_revenue = forms.IntegerField(label='Доход', max_value=1000000, min_value=0, widget=forms.TextInput(attrs={"placeholder": "Персональный доход в месяц*"}))
    education = forms.TypedChoiceField(label='Образование', choices=((1, "Начальное, среднее"), (2, "Неполное высшее"), (3, "Высшее"), (4, "Второе высшее"), (5, "Ученая степень")))
    family_status = forms.TypedChoiceField(label="Семейное положение", choices=((1, "Холост/не замужем"), (2, "Разведен(а)"), (3, "Гражданский брак"), (4, "Женат/замужем"), (5, "Вдовец/вдова")))
    foreign_passport = forms.BooleanField(label='Есть загран паспорт', required=False)
    car = forms.TypedChoiceField(label="Автомобиль", choices=((1, "Нет"), (2, "Отечественный"), (3, "Инномарка")))
    pledge = forms.TypedChoiceField(label="Залог для кредита", choices=((1, "Нет"), (2, "Авто"), (3, "Недвижимость")), required=False)



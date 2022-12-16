from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomerPostFrom(forms.Form):
    fullname = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={"placeholder": "Ivanov Ivan Ivanovich"}), max_length=150)
    birthday = forms.DateField(label='Дата Рождения', widget=forms.SelectDateWidget(empty_label=(("Choose Month", "Choose Day", "Choose Year")), years=range(1934, 2005)))
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = forms.CharField(label="Телефон", validators=[phoneRegex], max_length=12, widget=forms.TextInput(attrs={"placeholder": "+7 923 456 7890"}), min_length=12)
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"placeholder": "IvanIvanov@domain.ru"}), max_length=150)
    passport = forms.CharField(label='Паспорт', widget=forms.TextInput(attrs={'placeholder': '00 11 123456'}))
    payment_system = forms.TypedChoiceField(label="Платежная система", choices=((1, "Visa"), (2, 'MasterCard'), (3, 'Мир'), (4, 'American Express'), (5, 'Maestro'), (6, 'China UnionPay'), (7, 'УЭК')))
    currency = forms.TypedChoiceField(label="Валюта", choices=((1, 'Рубли'), (2, 'Евро'), (3, 'Доллар')))
    secret_code = forms.CharField(label='Секретный код', max_length=4, min_length=4, widget=forms.PasswordInput)

class MortgagePostForm(forms.Form):
    cost = forms.IntegerField(label="Цена недвижимости, ₽", max_value=1000000000, widget=forms.TextInput(attrs={"placeholder": "3 500 000"}))
    contribution = forms.IntegerField(label="Первоначальный взнос, ₽", max_value=100000000, widget=forms.TextInput(attrs={"placeholder":"700 000"}))
    term = forms.IntegerField(label="Срок кредита, лет", max_value=25, min_value=1, widget=forms.TextInput(attrs={"placeholder": "25"}))
    fullname = forms.CharField(label="ФИО", max_length=50, widget=forms.TextInput(attrs={"placeholder": "Ivanov Ivan Ivanovich"}))
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = forms.CharField(label="Телефон", validators=[phoneRegex], max_length=12, min_length=12, widget=forms.TextInput(attrs={"placeholder": "+7 923 456 7890"}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"placeholder": "IvanIvanov@domain.ru"}), max_length=150)
    birthday = forms.DateField(label="Дата рождения", widget=forms.SelectDateWidget(years=range(1934, 2005)))
    passport = forms.CharField(label='Паспорт', widget=forms.TextInput(attrs={'placeholder': '00 11 123456'}))

class DepositForm(forms.Form):
    deposit = forms.IntegerField(label='Размер вклада', min_value=25000, max_value=100000000, widget=forms.TextInput(attrs={"placeholder": "25000"}))
    term = forms.IntegerField(label='Срок вклада, мес.',min_value=3, max_value=36, widget=forms.TextInput(attrs={"placeholder": "3"}))
    currency = forms.TypedChoiceField(label="Валюта", choices=((1, 'Рубли'), (2, 'Евро'), (3, 'Доллар')))
    fullname = forms.CharField(label='ФИО', max_length=50, widget=forms.TextInput(attrs={"placeholder": "Ivanov Ivan Ivanovich"}))
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = forms.CharField(label='Телефон', validators=[phoneRegex], max_length=12, widget=forms.TextInput(attrs={"placeholder": "+7 923 456 7890"}))
    birthday = forms.DateField(label='Дата Рождения', widget=forms.SelectDateWidget(years=range(1934, 2005)))
    passport = forms.CharField(label='Паспорт', widget=forms.TextInput(attrs={'placeholder': '00 11 123456'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"placeholder": "IvanIvanov@domain.ru"}))
    percents_on_account = forms.BooleanField(label='Зачислять процент на счет', required=False)

class CreditForm(forms.Form):
    amount = forms.IntegerField(label='Сумма кредита', widget=forms.TextInput(attrs={"placeholder": '1000000'}), max_value=20000000)
    term = forms.IntegerField(label='Срок кредита', min_value=1, max_value=18, widget=forms.TextInput(attrs={'placeholder': "15"}))
    target = forms.TypedChoiceField(label='Цель кредита', choices=((1, 'Ремонт'), (2, 'Покупка недвижимости'), (3, 'Покупка авто'), (4, 'Погашение кредита'), (5, 'Развитие бизнеса'), (6, 'Лечение'), (7, 'Путешествие'), (8,'Иное')))
    fullname = forms.CharField(label='ФИО', max_length=50, widget=forms.TextInput(attrs={"placeholder": "Ivanov Ivan Ivanovich"}))
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = forms.CharField(label='Телефон', validators=[phoneRegex], max_length=12, widget=forms.TextInput(attrs={"placeholder": "+7 923 456 7890"}), min_length=12)
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"placeholder": "IvanIvanov@domain.ru"}))
    passport = forms.CharField(label='Паспорт', widget=forms.TextInput(attrs={'placeholder': '00 11 123456'}))
    birthday = forms.DateField(label='Дата Рождения', widget=forms.SelectDateWidget(years=range(1934, 2005)))
    personal_revenue = forms.IntegerField(label='Доход', max_value=1000000, min_value=0, widget=forms.TextInput(attrs={"placeholder": "Персональный доход*"}))
    education = forms.TypedChoiceField(label='Образование', choices=((1, "Начальное, среднее"), (2, "Неполное высшее"), (3, "Высшее"), (4, "Второе высшее"), (5, "Ученая степень")))
    family_status = forms.TypedChoiceField(label="Семейное положение", choices=((1, "Холост/не замужем"), (2, "Разведен(а)"), (3, "Гражданский брак"), (4, "Женат/замужем"), (5, "Вдовец/вдова")))
    foreign_passport = forms.BooleanField(label='Есть загран паспорт', required=False)
    car = forms.TypedChoiceField(label="Автомобиль", choices=((1, "Нет"), (2, "Отечественный"), (3, "Инномарка")))
    pledge = forms.TypedChoiceField(label="Залог для кредита", choices=((1, "Нет"), (2, "Авто"), (3, "Недвижимость")), required=False)

import datetime

today = datetime.datetime.today()
userBday = input('Enter your date of birth in DD/MM/YYYY format')
sBday = userBday.split('/')
Jbday = ""
Ajoined = Jbday.join(sBday)
Sjoined = ''
if ' ' in userBday:
    Sjoined = userBday.replace(' ', '')

def ChangeToDate():
    if len(Ajoined) == 8:
        bdd = datetime.datetime.strptime(Ajoined, '%d%m%Y')
        age = today - bdd
        print(f'your are {age.days/365 :.2f} years old')
    elif len(Sjoined) == 8:
        bdd1 = datetime.datetime.strptime(Sjoined, '%d%m%Y')
        age1 = today - bdd1
        print(f'your are {age1.days/365 :.2f} years old')
    elif len(Ajoined) != 8:
        print('you have entered invalid format date')
    elif len(Sjoined) != 8:
        print('you have entered invalid format date')

ChangeToDate()
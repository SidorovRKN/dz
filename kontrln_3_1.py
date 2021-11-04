# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
def credit_card(string):
    if string.isalnum:
        a = '**** **** **** ' + string[12:]
        return a
    else:
        return 'error'


num = input()
print(credit_card(num))
print('РАСИЯ')

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
def palindrome(string):
    if type(string) is str:
        counter = 1
        for i in range(len(string) - 1):
            if string[i] == string[-(i + 1)]:
                counter += 1
        if counter == len(string):
            return True
        else:
            return False


stroka = input()
print(palindrome(stroka))
print('РАСИЯ')
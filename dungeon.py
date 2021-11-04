import json
import sys


def finder(dict_name):
    lst = []
    for index_1 in dict_name:
        for index_2 in dict_name[index_1]:
            if type(index_2) is dict:
                lst.append(index_2)
    return lst


def opener(dict_base, lst_index):
    dict_search = finder(dict_base)[lst_index]
    name_loc = tuple(dict_search.keys())[0]
    field_names[0] = name_loc
    field_names[2] -= float(name_loc[name_loc.find('m') + 1:])
    with open('journal.txt', mode='a') as journal:
        str_field_names = field_names.copy()
        str_field_names[1], str_field_names[2] = str(field_names[1]), str(field_names[2])
        journal.write('__'.join(str_field_names))
        journal.write('\n')
    print(field_names)
    return dict_search


def fight(dit, num, list_or_not):
    if list_or_not == 'not':
        name = dit[tuple(dit.keys())[0]][num]
    elif list_or_not == 'list':
        name = dit[tuple(dit.keys())[0]][0][num]
    else:
        print('error')
    print('сейчас вы ведете бой с ', name)
    exp = name[name.find('p') + 1:name.find('_t')]
    tm = name[name.find('m') + 1:]
    if type(field_names[1]) is int:
        field_names[1] += int(exp)
    else:
        field_names[1] = int(exp)
    field_names[2] -= float(tm)
    print('монстр убит \n')
    with open('journal.txt', mode='a') as journal:
        str_field_names = field_names.copy()
        str_field_names[1], str_field_names[2] = str(field_names[1]), str(field_names[2])
        journal.write('__'.join(str_field_names))
        journal.write('\n')
    print(field_names)


def while_fight(count, fight_loc, list_or_not):
    counter = 0
    while counter < count:
        comand = input(':__')
        if comand == 'continue':
            if list_or_not == 'not':
                fight(fight_loc, counter, list_or_not='not')
            elif list_or_not == 'list':
                fight(fight_loc, counter, list_or_not='list')
            else:
                break
            counter += 1
            if counter == count:
                print('вы убили всех монстров тут ')
        elif comand == 's':
            print('вы вышли из режима битвы\n')
            break


with open('journal.txt', mode='w') as fil:
    fil.flush()

remaining_time = '1234567890.0987654321'
field_names = ['current_location', 'current_experience', 'current_date']
field_names[2] = float(remaining_time)

with open('rpg.json') as file:
    data = json.load(file)
field_names[0] = tuple(data.keys())[0]
print('____Вы в локации 0, тут есть моб, входы в локации 1 и 2____________________________\n'
      '____что бы убить моба введите fight, что бы пойти в другие локации введите 1 или 2_\n'
      '____для выхода введите s___________________________________________________________\n')

while True:

    command = input(':__')
    if command == 'fight':
        fight(data, 0, list_or_not='not')
        print('____Теперь вам осталось выбрать в какой проход пойти_\n'
              '____Введите 1 или 2__________________________________\n')
    elif command == '1':
        dit_1 = opener(data, 0)
        print('____Вы вошли в локацию 1___________________________________________________\n'
              '____Тут два одинаковых моба________________________________________________\n'
              '____что бы атаковать их введите fight______________________________________\n'
              '____так же тут проход в следущую локацию, что бы попасть в нее введите 3___\n')
        while True:
            command = input(':__')
            if command == 'fight':
                print('____Вы в режиме битвы, что бы выйти из него введите s________\n'
                      '____что бы продолжить битву с монстрaми ведите continue______\n'
                      '____всего тут находятся 2 монстра____________________________\n')
                while_fight(2, dit_1, list_or_not='not')
            elif command == '3':
                dit_3 = opener(dit_1, 0)
                print('____Вы вошли в локацию 3, тут есть только вход в локацию 7, что бы пойти туда, введите 7\n'
                      '____(для выхода из игры введите s)______________________________________________________\n')
                command = input(':__')
                if command == '7':
                    dit_7 = opener(dit_3, 0)
                    print('____Вы вошли в локацию 7, но тут опять только вход в следущую локацию\n'
                          '____что бы пойти в нее, введите 10___________________________________\n'
                          '____что б выйти из игры введите s____________________________________\n')
                    command = input(':__')
                    if command == 's':
                        print(field_names)
                        sys.exit()
                    elif command == '10':
                        dit_10 = opener(dit_7, 0)
                        print('____Вы вошли в локацию 10________________\n'
                              '____тут 4 разных моба____________________\n'
                              '____что бы начать бой введите fight______\n'
                              '____так же тут есть проход в локацию 12__\n'
                              '____что бы пойти туда, введие 12_________\n'
                              '____что б выйти из игры введите s________\n')
                        while True:
                            command = input(':__')
                            if command == 'fight':
                                print('____Вы в режиме битвы, что бы выйти из него введите s________\n'
                                      '____что бы продолжить битву уже с монстрaми введите continue_\n'
                                      '____всего тут находятся 4 монстра____________________________\n')
                                while_fight(4, dit_10, list_or_not='list')
                                print(
                                    '____Теперь вам осталось либо двинутся дальше (введите 12), либо выйти (введите s')
                            elif command == 's':
                                print(field_names)
                                sys.exit()
                            elif command == '12':
                                dit_12 = opener(dit_10, 0)
                                print('____Вы вошли в локацию 12 - тут два босса_\n'
                                      '____что бы вступить в бой введите fight___\n'
                                      '____что бы выйти введите s________________\n')
                                while True:
                                    command = input(':__')
                                    if command == 's':
                                        print(field_names)
                                        sys.exit()
                                    elif command == 'fight':
                                        print('____Вы в режиме битвы, что бы выйти из него введите s________\n'
                                              '____что бы продолжить битву уже с монстрaми введите continue_\n'
                                              '____всего тут находятся 2 монстра____________________________\n')
                                        while_fight(2, dit_12, list_or_not='not')
                                        print(
                                            f'__|||Вы дошли до конца подземелья и убили всех монстров в выбранном вами направлении|||__'
                                            f'{field_names}')
                                        sys.exit()

    elif command == '2':
        dit_2 = opener(data, 1)
        print('____Вы вошли в локацию 2_______________________________________________________________\n'
              '____Тут есть один моб__________________________________________________________________\n'
              '____что бы атаковать введите fight_____________________________________________________\n'
              '____так же тут проходы в локации 4, 5 и 6 (введите номер локации что бы войти в нее)___\n')
        while True:
            command = input('::__')
            if command == 'fight':
                fight(dit_2, 0, 'not')
                print(
                    '(монстров больще нет)тут проходы в локации 4, 5 и 6 (введите номер локации что бы войти в нее)___\n')
            elif command == 's':
                print(field_names)
                sys.exit()
            elif command == '4':
                dit_4 = opener(dit_2, 0)
                print('____Вы вошли в локацию 4_______________\n'
                      '____Тут 4 моба_________________________\n'
                      '____что бы атаковать их введите fight__\n'
                      '____что бы выйти из игры, введите s____\n')
                while True:

                    command = input('::__')
                    if command == 'fight':
                        print('____Вы в режиме битвы, что бы выйти из него введите s________\n'
                              '____что бы продолжить битву уже с монстрaми введите continue_\n'
                              '____всего тут находятся 3 монстра____________________________\n')
                        while_fight(3, dit_4, list_or_not='not')
                        print('____Все монстры убиты, но вы зашли в тупик___')
                        print(field_names)
                        sys.exit()
                    elif command == 's':
                        sys.exit()
            elif command == '5':
                dit_5 = opener(dit_2, 1)
                print('____Вы вошли в локацию 5________________\n'
                      '____Тут проходы в локации 8 и 9_________\n'
                      '____что бы пройти, введите номер локации\n'
                      '____что бы выйти из игры, введите s_____\n')
                while True:
                    command = input('::__')
                    if command == 's':
                        print(field_names)
                        sys.exit()
                    elif command == '8':
                        while True:
                            dit_8 = opener(dit_5, 0)
                            print('____Вы вошли в локацию 8_________________\n'
                                  '____Тут 5 монстров_______________________\n'
                                  '____что бы вступить в бой, введите fight_\n'
                                  '____что бы выйти из игры, введите s______\n')
                            command = input('::__')
                            if command == 'fight':
                                print('____Вы в режиме битвы, что бы выйти из него введите s________\n'
                                      '____что бы продолжить битву уже с монстрaми введите continue_\n'
                                      '____всего тут находятся 5 монстра____________________________\n')
                                while_fight(5, dit_8, list_or_not='not')
                                print(
                                    '____ВСЕ МОНСТРЫ УБИТЫ, НО ВЫ ПОДСКАЛЬЗНУЛИСЬ НА ГОВНЕ И Ж̷̢̭̮͚̎̾̋̍̀И̷͖̲̥̻͔͒͊̅̇̕Д̸̼̭̲̼̇͐͋͊̇͜К̵̮͍̯̘͕̋̀̇О̷̬͖̔̓̐̽̚ ̶̳̯̫̗͉̊̇П̷̧͎̜̬̙͆͝Е̶̧̳̎̽̀̀Р̸̹̪̯͔͓̀̈́͒Н̷̡̙̖͔̼̎͑̽̔Ў̵̼̺́͛͆̑В̷̪͎̻̋,̸̞̤̦͐͗̔ ̴̼̬̘̞̅̑̅͒У̴̪̬̰̼̉̑̅М̴̜̙̰͉̈́̌̊Е̸̱̫̖̾̅̆̓Р̴̡̩̌̅͋Л̴̝̦̯͍̭͒́И̷̗̦̺̏́')
                                sys.exit()
                            elif command == 's':
                                print(field_names)
                                sys.exit()
                    elif command == '9':
                        dit_9 = opener(dit_5, 1)
                        print('____Вы вошли в локацию 9___________________\n'
                              '____Тут 1 монстр и проход в локацию 11_____\n'
                              '____что бы вступить в бой, введите fight___\n'
                              '____что бы пойти в след. локацию введите 11\n'
                              '____что бы выйти из игры, введите s________\n')
                        while True:

                            command = input('::__')
                            if command == 'fight':
                                fight(dit_9, 0, list_or_not='not')
                            elif command == 's':
                                print(field_names)
                                sys.exit()
                            elif command == '11':
                                dit_11 = opener(dit_9, 0)
                                print('____Вы вошли в локацию 11__________________\n'
                                      '____Тут 1 монстр-босс и проход в локацию В2\n'
                                      '____что бы вступить в бой, введите fight___\n'
                                      '____что бы пойти в след. локацию введите В2\n'
                                      '____что бы выйти из игры, введите s________\n')
                                while True:
                                    command = input('::__')
                                    if command == 'fight':
                                        fight(dit_11, 0, list_or_not='not')
                                    elif command == 's':
                                        print(field_names)
                                        sys.exit()
                                    elif command == 'b2' or command == 'B2':
                                        dit_b2 = opener(dit_11, 0)
                                        print('____Вы вошли в локацию B2__________________\n'
                                              '____Тут 3 монстра__________________________\n'
                                              '____что бы вступить в бой, введите fight___\n'
                                              '____что бы выйти из игры, введите s________\n')
                                        while True:
                                            command = input("::__")
                                            if command == 'fight':
                                                print('____Вы в режиме битвы, что бы выйти из него введите s________\n'
                                                      '____что бы продолжить битву уже с монстрaми введите continue_\n'
                                                      '____всего тут находятся 3 монстра____________________________\n')
                                                while_fight(3, dit_b2, list_or_not='not')
                                                print(field_names)
                                                print(
                                                    '__|||Вы дошли до конца подземелья и убили всех монстров в выбранном вами направлении|||__')
                                                sys.exit()
                                            elif command == 's':
                                                print(field_names)
                                                sys.exit()
            elif command == '6':
                dit_6 = opener(dit_2, 2)
                print('____Вы вошли в локацию 6______________________\n'
                      '____Тут 1 монстр-босс и вход в локацию В1_____\n'
                      '____что бы вступить в бой, введите fight______\n'
                      '____что бы перейти в след. локацию, введите В1\n'
                      '____что бы выйти из игры, введите s___________\n')
                while True:
                    command = input('::__')
                    if command == 's':
                        print(field_names)
                        sys.exit()
                    elif command == "fight":
                        fight(dit_6, 0, list_or_not='not')
                    elif command == 'B1' or command == 'b1':
                        dit_b1 = opener(dit_6, 0)
                        print('____Вы вошли в локацию B1_______________\n'
                              '____Тут 5 монстров______________________\n'
                              '____что бы вступить в бой, введите fight\n'
                              '____что бы выйти из игры, введите s_____\n')
                        while True:
                            command = input('::__')
                            if command == 'fight':
                                print('____Вы в режиме битвы, что бы выйти из него введите s________\n'
                                      '____что бы продолжить битву уже с монстрaми введите continue_\n'
                                      '____всего тут находятся 5 монстров___________________________\n')
                                while_fight(5, dit_b1, list_or_not='not')
                                print(field_names)
                                print(
                                    'Вы зашли в тупик и нашли _РА СИ Я_РА СИ Я_РА СИ Я_РА СИ Я_РА СИ Я_РА СИ Я_РА СИ Я_')
                                sys.exit()
                            elif command == 's':
                                print(field_names)
                                sys.exit()

    elif command == 's':
        print(field_names)
        break

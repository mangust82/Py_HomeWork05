# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более
# чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько 
# конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
from time import sleep

# Проверка конца игры 
def check_win(rest):
    if rest <= 0:
        return True
    else:
        return False

# Ход игроков
def take_candy(player):
    print(f'Ход {player}')
    while (True):
        try:
            candy = int(input("возьмите конфеты не более 28: "))
            if candy >= 1 and candy <= 28:
                break
            else:
                print('введите корректное значение.') 
        except ValueError:
            print('вы ввели некорректное значение попробуйте ещё раз.')
    return candy

# умниый ход бота
def smart_move(rest, candy):
    candy = rest % 29 if rest != 0 else random.randint(1, 28)
    print(f'Ход бота: {candy}')
    return candy

# обычный ход бота
def take_candy_bot():
    sleep(1)
    # candy = smart_move(rest)
    while (True):
        candy = random.randint(1,9)
        if candy >= 1 and candy <= 28:
            print(f'Ход бота: {candy}')
            break 
    return candy

# Игра человек-человек
def manman(rest):
    print('Cтарт игры человек-человек:\n')
    while rest > 0:
        rest -= take_candy('игрока 1')
        print(rest)
        if check_win(rest):
            print('победил игрок 1')
            break
        rest -= take_candy('игрока 2')
        print(rest)
        if check_win(rest):
            print('победил игрок 2')
            break

# Игра человек-бот
def botman(rest):
    print('Cтарт игры бот-человек:\n')
    while rest > 0:
        candy1 = take_candy('человека')
        rest -= candy1
        print(rest)
        if check_win(rest):
            print('победил человек')
            break
        rest -= smart_move(rest, candy1)
        print(rest)
        if check_win(rest):
            print('победил бот')
            break

# Игра человек-бот продвинутый уровень
def botman_hightlevel(rest):
    print('Cтарт игры бот-человек:\n')
    while rest > 0:
        candy1 = take_candy('человека')
        rest -= candy1
        print(rest)
        if check_win(rest):
            print('победил человек')
            break
        rest -= smart_move(rest, candy1)
        print(rest)
        if check_win(rest):
            print('победил бот')
            break

print('Выберете режим игры: \n1. Человек-Человек\n2. Человек-компьютер')
print('3. Человек-компьютер продвинутый уровень')
game = int(input('Введите режим: '))
if game == 1:
    manman(250)
elif game == 2:
    botman(250)
elif game == 3:
    botman_hightlevel(250)

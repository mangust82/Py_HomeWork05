# Создайте программу для игры в ""Крестики-нолики"".

from os import system
from time import sleep
import random

# Рисуем шаблон поля
def CoordXO():
    system('cls')
    print("\033[4m{}".format('1|2|3\n4|5|6\n') + "7|8|9\n")

# Рисуем ход 
def PrinXO(XOlist):
    for el in XOlist:
        for i in el:
            print(f"\033[4m{i}{'|'}", end="")
        print()

# Заносим ход игрока(X) и бота(0) в список 
def XorO(XOlist, move, XO):
    for i in range(len(XOlist)):
        for j in range(len(XOlist[i])):
            if j+1+3*i == move:
                XOlist[i][j] = XO
    return XOlist

# Ход игрока с проверкой допустимых значений в списке
def my_move(XOlist):
    while True:
        try:
            inmum = int(input('Сделайте ваш ход: '))
            if inmum < 1 or inmum > 9:
                print('Введите правильные координаты поля')
            else:
                b = list(inner for gpoup in XOlist for inner in gpoup)
                ind = []
                for i in range(len(b)):
                    if b[i] == 'X' or b[i] == '0':
                        ind.append(str(i+1))
                if str(inmum) in ind:
                    print('Это поле уже занято. Сходите ещё раз')
                else:
                    CoordXO()
                    PrinXO(XorO(XOlist, inmum, 'X'))
                    break
        except:
            print('Введите корректное значение')

# Ход бота
def bot_move(XOlist):
    while True:
        sleep(0)
        CoordXO()
        print('Я тоже сходил')
        move = good_move(XOlist)
        b = list(inner for gpoup in XOlist for inner in gpoup)
        ind = []
        for i in range(len(b)):
            if b[i] == 'X' or b[i] == '0':
                ind.append(str(i+1))

        if str(move) not in ind:
            PrinXO(XorO(XOlist, move, '0'))
            break
        else:
            while str(move) in ind:
                move = random.randint(1,9)
            PrinXO(XorO(XOlist, move, '0'))
            break

# Наделяем бот некоторым интеллектом. Ищем более лучшие ходы
def good_move(XOlist):
    x = 5
    for i in range(len(XOlist)):
        for j in range(len(XOlist[i])):
            if XOlist[i][j]  == " " and XOlist[i].count('X') == 2:
                x = j+1+3*i
    transp =list(zip(XOlist[0], XOlist[1], XOlist[2]))
    for i in range(len(transp)):
        for j in range(len(transp[i])):
            if transp[i][j]  == " " and transp[i].count('X') == 2:
                x = i+1+3*j
    return x

# Проверка конца игры
def CheckEndOfgame(XOlist):
    b = list(inner for gpoup in XOlist for inner in gpoup)
    for hor in XOlist:
        if hor.count('X') == 3:
            print('\nВы выиграли!!!')
            exit()
        elif hor.count('0') == 3:
            print('\nВы проиграли!!!')
            exit()
    for ver in zip(XOlist[0], XOlist[1], XOlist[2]):
        if ver.count('X') == 3:
            print('\nВы выиграли!!!')
            exit()
        elif ver.count('0') == 3:
            print('\nВы проиграли!!!')
            exit()
    if b[0] == b[4] == b[8] == 'X' or b[2] == b[4] == b[6] == 'X':
        print('\nВы выиграли!!!')
        exit()
    elif b[0] == b[4] == b[8] == '0' or b[2] == b[4] == b[6] == '0':
        print('\nВы проиграли!!!')
        exit()
    elif ' ' not in b:
            print('\nНичья!')
            exit()

XOlist = [[' ',' ',' '] for i in range(3) ]
CoordXO()
PrinXO(XOlist)

while(True):
    my_move(XOlist)
    CheckEndOfgame(XOlist)
    bot_move(XOlist)
    CheckEndOfgame(XOlist)


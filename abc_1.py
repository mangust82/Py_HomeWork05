# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def del_abc(path_file):
   with open(path_file, "r+", encoding='utf-8') as f1_obj:
    with open('абв_out.txt', 'w', encoding='utf-8') as f2_obj:
        for line in f1_obj.readlines():
            a = line.split(' ')
            for  el in a:
                if el.find('абв') != -1:
                    a.pop(a.index(el))
            ' '.join(a)
            print(' '.join(a), file=f2_obj, end='')

del_abc('абв_in.txt')

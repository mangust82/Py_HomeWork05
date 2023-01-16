# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def pck_rle(in_file):
    with open(in_file, 'r') as rle_in:
        with open('rle_out.txt', 'w') as rle_out:
            count = 1
            for el in rle_in.readlines():
                res_str = ''
                for i in range(1, len(el)):
                    if el[i] == el[i-1] and i != len(el)-1:
                        count += 1
                    else:
                        res_str += str(count) + el[i-1]
                        count = 1
                print(res_str, file = rle_out)



def unpck_rle(in_file):
    str = ''
    with open('rle_unpc.txt', 'w') as rle_out:
        with open(in_file, 'r') as rle_in:
            for elstr in rle_in.readlines():
                for el in elstr:
                    if el.isdigit():
                        str += el
                    elif el.isspace():
                        print(el, end = '', file=rle_out)
                    else:
                        print(el*int(str), end ='', file=rle_out)
                        str = ''

pck_rle('rle_in.txt')
unpck_rle('rle_out.txt')
        
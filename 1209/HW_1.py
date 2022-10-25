'''Написать программу, которая считает процент подстрок, в которых больше заглавных букв.
На вход подаётся большая строка, подстроки в которой перечислены через пробел. 
Примеры: 'ABc dbE FRl Ama' -> 50%, 'NDp Lka nuR vtE' -> 25%
'''


def line_count(line):
    line_split = line.split()
    upper = 0
    for el_1 in line_split:
        upper_local = 0
        for el_2 in el_1:
            if el_2.isupper():
                upper_local += 1
        if upper_local > len(el_1) - upper_local:
            upper = upper + 1
    return str(int(upper / len(line_split) * 100)) + '%'

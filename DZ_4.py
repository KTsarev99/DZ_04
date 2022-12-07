# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import random

import itertools

k = int(input('натуральная степень k =:'))

def random_list(n:int):#n = количество элементов 
    list1 = range(0,n)
    list2 =[]
    for i in list1:
        i = random.randint(0, 101)
        list2.append(i)
    return list2   

print(random_list(k+1))


def get_polynomial(k, ratios):# 
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')

ratios = random_list(k+1)
polynom1 = get_polynomial(k, ratios)
print(polynom1)


with open("file_DZ4.txt", "w") as data:
    data.write(polynom1)



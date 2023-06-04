'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#Код на python. Функция заполнения массива случайными числами
from random import random
N = 10
def func(a,mn,mx):
    for i in range(N):
        a[i] = int(random() * (mx-mn+1)) + mn

a = [0] * N
x = int(input('Введите начало диапазона '))
y = int(input('Введите конец диапазона '))
func(a,x,y)
print(a)

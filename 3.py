# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform
from random import randint


spisok = []
spisok2 = []

for i in range(randint(2, 5)):
    spisok.append(round(uniform(0, 100), 2))       #("%.3f" % j)[:-1])
print(spisok)

for i in spisok:
    spisok2.append(round((i - int(i)), 2))
print(spisok2)

print("разница между max и min =", round((max(spisok2) - min(spisok2)), 2))







# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


spisok = []
for i in range(randint(2, 10)):
    spisok.append(randint(0, 10))
print(spisok)  

sum = 0
for i in range(len(spisok)):
    if i % 2 != 0:
        sum = sum + spisok[i]
        
print(sum)



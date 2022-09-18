# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


spisok = []
spisok2 = []

for i in range(randint(2, 10)):
    spisok.append(randint(0, 10))
print(spisok)

if len(spisok) % 2 == 0:
    for i in range(len(spisok) // 2):
        spisok2.append(spisok[i] * spisok[len(spisok) - i - 1])
else:
    for i in range(len(spisok) // 2):
        spisok2.append(spisok[i] * spisok[len(spisok) - i - 1])
    spisok2.append((spisok[len(spisok) // 2]) * 2)
print(spisok2)
    
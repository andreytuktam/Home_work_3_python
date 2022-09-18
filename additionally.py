# Суперсдвиг
# (Время: 1 сек. Память: 16 Мб Сложность: 20%)
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю 
# последовательность (сдвиг - циклический) на |K| элементов вправо, если 
# K – положительное и влево, если отрицательное.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N, во второй 
# строке записаны N целых чисел Ai, а в последней – 
# целое число K. (1 ≤ N ≤ 105, |K| ≤ 105, |Ai| ≤ 100).

# Выходные данные
# В выходной файл OUTPUT.TXT выведите полученную последовательность.


from random import randint


n = 5 #randint(1, 106)
spisok1 = []
spisok2 = [0] * n

for i in range(n):
    spisok1.append(randint(1, 101))
print(spisok1)

k = randint(-n, n) 
print(k)
k = k % n

if k > 0:
    for i in range(k):
        spisok2[i] = spisok1[n - k + i]
    for i in range(n - k):
        spisok2[k + i] = spisok1[i]
    print(spisok2)
else:
    k = -k
    for i in range(k):
        spisok2[i] = spisok1[n - k + i]
    for i in range(n - k):
        spisok2[k + i] = spisok1[i]
    print(spisok2)
        



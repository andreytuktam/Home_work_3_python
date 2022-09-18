# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных 
# индексов.(Доп)
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(n):
    if (n <= 1):
        return n
    else:
        return (fib(n-1) + fib(n-2))
n = int(input("n = "))
f1 = []
f2 = []
for i in range(n):
    f1.append(fib(i))
for i in range(len(f1)):
    if i % 2 == 0:
        f2.append(f1[i] * (-1))
    else:
        f2.append(f1[i])
f2 = list(reversed(f2))[:len(f1) - 1]
print(f2 + f1)
    




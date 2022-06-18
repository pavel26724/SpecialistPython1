# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here

import random
numbers = []
n = 4
i = 0

for i in range(n):
    number = random.randint(-10, 10)
    numbers.append(number)
print(numbers)

summa = 0
for number in numbers:
    summa += number

print(summa)

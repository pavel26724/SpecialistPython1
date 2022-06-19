def even(...):
    ...
    return ...

n = ...
if even(n):
   print("Число четное")
else:
   print("Число не четное")


def even(n):
    if n % 2 == 0:
        return (n)

n = int(input('Введи число с клавиатуры: '))
if even(n):
    print("Число четное")
else:
    print("Число не четное")

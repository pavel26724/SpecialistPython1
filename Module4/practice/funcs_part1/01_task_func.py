# Напишите функцию, возвращающую наибольшее из четырех чисел

def max4(n1, n2, n3, n4):
    # TODO: your code here
    pass


# Тестируем функцию
print(max2(5, 6, 12, 7))
print(max2(-10, -12, -4, -9))
print(max2(2.5, 2.6, 2.6, 2.4))
print(max2(-2.5, 0, -1.2, -0.4))
print(max2(-2, -2, -2, -2))


def max4(n1, n2, n3, n4):
    if n1 > n2 and n1>n3 and n1>n4:
        return(n1)
    elif n2 > n1 and n2>n3 and n2>n4:
        return(n2)
    elif n3 > n1 and n3>n1 and n3>n4:
        return(n3)
    else:
        return(n4)

# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 21, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -1, -2))

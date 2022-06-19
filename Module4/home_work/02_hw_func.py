# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    pass


# TODO: your code here
print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.


def distance(xa, ya, xb, yb, xc, yc):
    length_ab = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
    length_bc = ((xc - xb) ** 2 + (yc - yb) ** 2) ** 0.5
    length_ac = ((xc - xa) ** 2 + (yc - ya) ** 2) ** 0.5
    if length_ab < length_bc and length_ab < length_ac:
        length_ab = 'AB'
        return length_ab
    elif length_bc < length_ab and length_bc < length_ac:
        length_bc = 'BC'
        return length_bc
    else:
        length_ac = 'AC'
        return length_ac


distance(6, 10, 1332, 2025, 4, 222)
# TODO: your code here
print("Самый короткий отрезок:", distance(6, 10, 1332, 2025, 4, 222))  # Выводим название отрезка, например “АС”.

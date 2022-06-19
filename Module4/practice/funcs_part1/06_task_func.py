# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    # TODO: your code here
    pass

# Не забудьте протестировать вашу функцию


def point_in_circle(x, y, xc, yc, r):
    length = ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5
    if length < r:
        print('Точка внутри окружности')
    else:
        print('Точка вне окружности')

point_in_circle(9, 0.5, 4, 4, 3.75)

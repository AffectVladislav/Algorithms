    #   Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения:
    #   длину окружности и площадь круга, ограниченного данной окружностью.
from math import pi

def get_circle(radius):
    l = 2 * pi * radius
    a = pi * radius ** 2

    return l, a

#   считывает данные
r = float(input())

#   вызываем функцию
length, square = get_circle(r)
print(length, square)
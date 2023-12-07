    #   Напишите функцию is_valid_triangle(side1, side2, side3),
    #   которая принимает в качестве аргументов три натуральных числа, и возвращает значение True
    #   если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.
def is_valid_triangle(side1, side2, side3):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
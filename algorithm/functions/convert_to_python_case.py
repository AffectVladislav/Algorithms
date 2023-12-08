    #  Напишите функцию convert_to_python_case(text)
    #  которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

def convert_python_case(text):   # # объявление функции
    new_text = ""
    for el in text:
        if not el == el.lower():  # проверяем, что элемент в верхнем регистре (пропускаем цифры)
                new_text += "_" + el.lower()
        else:
                new_text += el

    return new_text[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_python_case(txt))

def convert_to_python_case(text):
    for x in text:
        if x.isupper():
            text = text.replace(x, '_' + x.lower())
    text = text[1:]
    return text
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
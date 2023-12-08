    #  Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
    #  состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной последовательностью
    #  и False в противном случае.
def is_correct_bracket(text):
    while "()" in text:
        text = text.replace("()", '')
    if text == '':
        return True
    return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
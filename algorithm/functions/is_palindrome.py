    #  Напишите функцию is_palindrome(text),
    #  которая принимает в качестве аргумента строку text
    #  и возвращает значение True если указанный текст является палиндромом и False в противном случае.

    #  Палиндром – это строка, которая читается одинаково в обоих направлениях
    #  При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.

def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
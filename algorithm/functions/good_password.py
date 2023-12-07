    #  Напишите функцию is_password_good(password),
    #  которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True,
    #  если пароль является надежным и False - в противном случае.

    #  Пароль является надежным если:
    # его длина не менее 8 символов;
    # он содержит как минимум одну заглавную букву (верхний регистр);
    # он содержит как минимум одну строчную букву (нижний регистр);
    # он содержит хотя бы одну цифру.

def is_password_good(password):
    if len(password) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for x in password:
        if x.isupper():
            flag1 = True
        elif x.islower():
            flag2 = True
        elif x.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
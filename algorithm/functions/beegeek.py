    # BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
    #
    # Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
    #
    # число a – должно быть палиндромом;
    # число b – должно быть простым;
    # число c – должно быть четным.
    # Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка и False - в противном случае.

def is_valid_password(password):
    x = password.split(':')
    if len(x) != 3:
        return False
    a, b, c = x[0], x[1], x[2]
    flag1, flag2, flag3 = False, False, False
    if a == a[::-1]:
        flag1 = True
    for i in range(2, int(b)):
        if int(b) % i == 0:
            return False
    flag2 = True
    if int(c) % 2 == 0:
        flag3 = True
    return flag1 and flag2 and flag3

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
    #   Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и возвращает значение True,
    #   если слова имеют одинаковую длину и отличаются ровно в одном символе и False  в противном случае.

def is_one_away(word1, word2):
    counter = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                counter += 1
        if counter + 1 == len(word1):
            return True
    return False

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
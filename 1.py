# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = "оыватпло лыабвва ывлабвдо ывдлытпл ывдалт ывл"
my_list = my_str.split(" ")
result = []

for word in my_list:
    if "абв" not in word:
        result.append(word)

print(" ".join(result))
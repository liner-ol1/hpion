from a2 import *
from a3 import times
from a3 import minutes



name = input("Введите ваше имя: ")
namemi = "Привет, " + name + "! Добро пожаловать в программу для шпионов!"
print(namemi)
print ("Теперь время для шифрования!")
a = replace_letters()
print("Теперь ваш текст выглядит так - ", a)
print ("Теперь время для шифрования!")
count = k
print("Теперь ваше слово выглядит так -  ", count)

print('Ещё я могу перевести минуты в часы и обратно')
hh = int(input("Введите кол-во часов, которое хотите перевести:"))
print(hh, "часов =", times(hh), "секунд.")
         
mm = int(input("Введите кол-во минут, которое хотите перевести: "))
print(mm, "минуту =", minutes(mm), "секунд.")

from a2 import *

name = input("Введите ваше имя: ")
namemi = "Привет, " + name + "! Добро пожаловать в программу для шпионов!"
print(namemi)
print ("Теперь время для шифрования!")
a = replace_letters()
print("Теперь ваш текст выглядит так - ", a)
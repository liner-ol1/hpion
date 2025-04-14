sentence = input("Введите предложение: ")
count = 0
for char in sentence:
    if ('А' <= char <= 'Я') or ('а' <= char <= 'я'):
        count += 1

#считает буквы в предложении

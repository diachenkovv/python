# Дяченко В.В, ЗПІ-18
# Написати програму, що рахує суму введених чисел

print("Вводьте числа для обрахунку суми.\nДля припинення вводу та виведення суми введіть 0.\n")

summ = 0  # сума
i = 1  # число

while i != 0:  # доки число не дорівнює 0,..
    i = int(input())
    summ += i  # вводити та додавати до суми

print("\nСума:", summ)  # вивести суму на екран

# \Дяченко В.В., ЗПІ-18
# Написати програму, що зчитує цілі числа з консолі по одному
# Числа перевіряються: меньше 10 ігноруються, більше 100 припиняють роботу циклу

n = 10  # число
i_put = ""  # змінна для остаточного виведення

while n <= 100:  # доки число не перевищить 100...
    n = int(input())  # вводиться число
    if n >= 10 and n <= 100:  # якщо число не менше 10...
        i_put += "\n" + str(n)  # воно додається до вивідної змінної

print(i_put)  # виведення результату

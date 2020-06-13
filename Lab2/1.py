# Дяченко В.В., ЗПІ-18

print("Введіть 2 числа та оберіть дію:\n -додавання (+)\n -відніманння (-)\n -ділення (/)\n -множення (*)\n -залишок від ділення (mod)\n -степінь (pow)\n -цілочисельне ділення (div)\n")

a = float(input("Число 1: "))  # Перше число
b = float(input("число 2: "))  # Друге число

diia = input("Що треба зробити?: ")  # Дія
# Далі відбуваються підрахунки:
if diia == "+":
    res = a + b
    print(res)
elif diia == "-":
    res = a - b
    print(res)
elif diia == "/" and b == 0:
    print("Ділення на 0! Хоча результат: ∞")
elif diia == "/" and b != 0:
    res = a / b
    print(res)
elif diia == "*":
    res = a * b
    print(res)
elif diia == "mod" and b == 0:
    print("Ділення на 0! Хоча результат: ∞")
elif diia == "mod" and b != 0:
    res = a % b
    print(res)
elif diia == "pow":
    res = a ** b
    print(res)
elif diia == "div" and b == 0:
    print("Ділення на 0! Але результат: ∞")
elif diia == "div" and b != 0:
    res = a // b
    print(res)
else:
    print("Щось неможливо знайти правильну команду :/")

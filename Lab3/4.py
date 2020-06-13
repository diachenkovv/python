# Лаб3, завд4, Дяченко В.В., ЗПІ-18
# Написати програму для визначення можливості ходу конем

input = open('input4.txt', 'r')  # відкриття файлу з вхідними даними
# відкриття порожнього файлу, куди буде надіслано результат
output = open('output4.txt', 'w')

l1 = input.read(1)
try:
    z1 = int(input.read(1))
except (TypeError, ValueError):
    print("Помилка!")
    output.write("Помилка!")
    exit(0)
d = input.read(1)
l2 = input.read(1)
try:
    z2 = int(input.read(1))
except (TypeError, ValueError):
    print("ПОМИЛКА!")
    output.write("ПОМИЛКА!")
    exit(0)  # Введення та перевірка даних

print(l1, z1, l2, z2)

if l1 == "A":
    int1 = 1
elif l1 == "B":
    int1 = 2
elif l1 == "C":
    int1 = 3
elif l1 == "D":
    int1 = 4
elif l1 == "E":
    int1 = 5
elif l1 == "F":
    int1 = 6
elif l1 == "G":
    int1 = 7
elif l1 == "H":
    int1 = 8
else:
    print("Помилочка")
    output.write("ПОМИЛКА!")
    exit(0)  # переведення значень з літер на цифри

if l2 == "A":
    int2 = 1
elif l2 == "B":
    int2 = 2
elif l2 == "C":
    int2 = 3
elif l2 == "D":
    int2 = 4
elif l2 == "E":
    int2 = 5
elif l2 == "F":
    int2 = 6
elif l2 == "G":
    int2 = 7
elif l2 == "H":
    int2 = 8
else:
    print("Ех... Помилка")
    output.write("Сталася помилка")
    exit(0)  # переведення значень з літер на цифри
# перевірка умови та виведення результату:
if ((abs(int1 - int2) <= 1 or abs(int1 - int2) <= 2) and (abs(z1 - z2) <= 1 or abs(z1 - z2) <= 2) and (abs(int1 - int2) != abs(z1 - z2)) and ((int1 != int2) and (z1 != z2))):
    print("ТАК")
    output.write("ТАК")
else:
    print("НІ!!")
    output.write("НІ!!")

input.close()  # закриття файлу з вхідними даними
output.close()  # закриття файлу з результатом

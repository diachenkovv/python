# Дяченко В.В., ЗПІ-18
# Написати програму, що перевіряє правильність множення

input = open('input2.txt', 'r')  # відкриття файлу з вхідними даними
# відкриття порожнього файлу, куди буде надіслано результат
output = open('output2.txt', 'w')

U = input.read().split()  # зчитування та заповнення масиву

print(U)

if int(U[0]) > 10 ** 2 or int(U[1]) > 10 ** 2 or int(U[2]) > 10 ** 6:  # перевірка діапазону
    output.write("Числа вийшли за рамки можливого!")
else:
    if int(U[0]) * int(U[1]) == int(U[2]):  # перевірка на правильність множення
        output.write("ТАК")
    else:
        output.write("НІ")

input.close()  # закриття файлу з вхідними даними
output.close()  # закриття файлу з результатом

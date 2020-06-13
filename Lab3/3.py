# Дяченко В.В., ЗПІ-18
# Написати програму, що визначає, чи отримає Василь четвірку за чверть (чи не отримає... чи отримає?)

input = open('input3.txt', 'r')  # відкриття файлу з вхідними даними
# відкриття порожнього файлу, куди буде надіслано результат
output = open('output3.txt', 'w')

n = input.readline()  # зчитування даних
n = n.rstrip()
n = int(n)  # конвертація в цілочисельний тип
i = 0  # лічильник (ні не електричний)
U = input.read().split()  # зчитування та заповнення масиву

i_ch = 0  # лічильник парних чисел
i_nch = 0  # лічильник непарних чисел
ch = ""  # змінна для виведення
nch = ""  # змінна для виведення
ans = ""  # змінна для виведення

print(n)
print(U)

for i in range(n):
    if int(U[i]) % 2 != 0:
        nch += str(U[i]) + " "
        i_nch += 1
    i += 1
print(nch)
output.write(nch + "\n")  # виведення непарних чисел
i = 0
for i in range(n):
    if int(U[i]) % 2 == 0:
        ch += str(U[i]) + " "
        i_ch += 1
    i += 1
print(ch)
output.write(ch + "\n")  # виведення парних чисел
if i_ch > i_nch:
    ans = "YES"
elif i_nch > i_ch:
    ans = "NO"
else:
    ans = "..."
print(ans)
output.write(ans)  # виведення відповіді на питання

input.close()  # закриття файлу з вхідними даними
output.close()  # закриття файлу з результатом

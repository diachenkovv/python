# Дяченко В.В, ЗПІ-18
# Винайти програму, що рахує квадрат числа, що закінчується на 5, альтернативним способом

input = open('input1.txt', 'r')  # відкриття файлу з вхідними даними
# відкриття порожнього (як моє життя...) файлу, куди буде надіслано результат
output = open('output1.txt', 'w')
n = int(input.read())  # зчитування даних
# перевірка умови (число має закінчуватись на 5)
if n % 10 == 5 and n < (4 * (10 ** 5)):
    res = (n // 10) * (n // 10 + 1) * 100 + 25  # обрахунки
    output.write(str(res))  # відправка результату у відповідний файл
else:
    # якщо число в файлі з вхідними даними не задовільняє умову, вивести відповідне повідомлення
    print("Число не відповідає умовам програми!")
input.close()  # закриття файлу з вхідними даними
output.close()  # закриття файлу з результатом

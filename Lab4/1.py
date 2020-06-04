#Лаб4, завд1, Карпенко Ю.О., ЗПІ-18
#Написати програму, що визначає найбільшу купу золотих монет

input = open('input1.txt', 'r') #відкриття файлу з вхідними даними
output = open('output1.txt', 'w') #відкриття порожнього файлу, куди буде надіслано результат

Golden_heaps = input.read().split() #зчитування та заповнення масиву
for i in range(3):
    Golden_heaps[i] = int(Golden_heaps[i]) #зміна типу елементів масиву

print(Golden_heaps)

output.write(str(max(Golden_heaps))) #Виведення максимального

input.close() #закриття файлу з вхідними даними
output.close() #закриття файлу з результатом
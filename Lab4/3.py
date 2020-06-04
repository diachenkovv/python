#Лаб4, завд3, Карпенко Ю.О., ЗПІ-18
#Написати програму, що обчислює сумудодатніх чисел та добуток всіх чисел крім найменшого та найбільшого

input = open('input3.txt', 'r') #відкриття файлу з вхідними даними
output = open('output3.txt', 'w') #відкриття порожнього файлу, куди буде надіслано результат

n = input.readline() #зчитування даних
n = n.rstrip()
n = int(n) #контертація в цілочисельний тип
i = 0 #лічильник

U = input.read().split() #зчитування та заповнення масиву
for i in range(n):
    U[i] = int(U[i]) #зміна типу елементів масиву

summ = 0 #сума
pr = 1 #добуток
res = "" #результат

print(n)
print(U)

i = 0
for i in range(n):
	if U[i] > 0:
		summ += U[i]
	i += 1
print(summ) #обчислення суми

i = 0
y = 0
u = 0
for i in range(n):
	if U[i] == min(U):
		y = i
	if U[i] == max(U):
		u = i
	i += 1
i = 0
for i in range(n):
	if (i > y and i < u) or (i < y and i > u):
		pr *= U[i]
	i += 1
print(pr) #обчислення добутку

res = str(summ) + " " + str(pr) #результат
output.write(res) #виведення результату

input.close() #закриття файлу з вхідними даними
output.close() #закриття файлу з результатом
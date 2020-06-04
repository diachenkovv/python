#Лаб2, завд1, Карпенко Ю.О., ЗПІ-18
#Написати простий калькулятор

print("Введіть 2 числа та оберіть дію:\n -додавання (+)\n -відніманння (-)\n -ділення (/)\n -множення (*)\n -залишок від ділення (mod)\n -степінь (pow)\n -цілочисельне ділення (div)\n")

a = float(input("число 1: ")) #Перше число
b = float(input("число 2: ")) #Друге число

dia = input("дія: ") #Дія
 #Далі відбуваються підрахунки:
if dia == "+":
	res = a + b
	print(res)
elif dia == "-":
	res = a - b
	print(res)
elif dia == "/" and b == 0:
	print("Ділення на 0!")
elif dia == "/" and b != 0:
	res = a / b
	print(res)
elif dia == "*":
	res = a * b
	print(res)
elif dia == "mod" and b == 0:
	print("Ділення на 0!")
elif dia == "mod" and b != 0:
	res = a % b
	print(res)
elif dia == "pow":
	res = a ** b
	print(res)
elif dia == "div" and b == 0:
	print("Ділення на 0!")
elif dia == "div" and b != 0:
	res = a // b
	print(res)
else:
	print("Неправильна або невідома команда!")
#Лаб2, завд3, Карпенко Ю.О., ЗПІ-18
#Вивести число програмістів з правильно зміненим словом "програміст"

n = int(input("кількість програмістів: ")) #к-ть програмістів

if n < 0: #визначення правильної форми:
	print("Хм... А це як? :)")
elif (n % 10 == 0) or (n % 10 >= 5 and n % 10 <= 9) or (n % 100 >= 11 and n % 100 <= 14):
	print(n, "програмістів")
elif n % 10 == 1:
	print(n, "програміст")
elif n % 10 >= 2 and n % 10 <= 4:
	print(n, "програмісти")
else:
	print("Помилка")
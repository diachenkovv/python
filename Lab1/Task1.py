# Дяченко В.В
print("Тимофій зазвичай спить вночі X годин і влаштовує собі вдень тиху годину на Y хвилин.\nВизначити, скільки всього хвилин на добу Тимофій спить.\n")

X = int(input("Годин: "))  # Скільки годин Тимофій спить вночі
Y = int(input("Хвилин: "))  # Скільки хвилин Тимофій спить удень
Res = X * 60 + Y  # Обрахунки (в хвилинах)

if Res >= 1440:  # Якщо кількість вхилин перевищує добову,..
    # виводиться відповідне повідомлення
    print("Вибач, але у добі не може перевищувати 1440 хвилин :/")
else:  # якщо ж все нормально,..
    print("\nТимофій спить", Res, "хвилин на добу.")  # виводиться результат

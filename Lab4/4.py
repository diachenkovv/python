#Лаб4, завд4, Карпенко Ю.О., ЗПІ-18
#Написати програму для кубічних рівнянь

input = open('input4.txt', 'r') #відкриття файлу з вхідними даними
output = open('output4.txt', 'w') #відкриття порожнього файлу, куди буде надіслано результат

U = input.read().split() #зчитування та заповнення масиву
for i in range(4):
    U[i] = int(U[i]) #зміна типу елементів масиву
k_a = U[0]
k_b = U[1]
k_c = U[2]
k_d = U[3]
a = k_b / k_a
b = k_c / k_a
c = k_d / k_a
q = (a**2 - 3 * b) / 9
r = (2 * a**3 - 9 * a * b + 27 * c) / 54
s = q**3 - r**2
res = ""
if s > 0:
    from math import acos, cos, sqrt, pi
    f = (1 / 3) * acos(r / sqrt(q**3))
    x1 = -2 * sqrt(q) * cos(f) - (a / 3)
    x2 = -2 * sqrt(q) * cos(f + (2 / 3) * pi) - (a / 3)
    x3 = -2 * sqrt(q) * cos(f - (2 / 3) * pi) - (a / 3)
    print("x1 = ", round(x1))
    print("x2 = ", round(x2))
    print("x3 = ", round(x3))
    res = str(round(x1)) + " " + str(round(x2)) + " " + str(round(x3))
elif s < 0:
    if q > 0:
        from cmath import acosh, cosh, sinh, sqrt
        f = (1 / 3) * acosh((abs(r)) / (sqrt(q**3)))
        if r > 0:
            x1 = -2 * sqrt(q) * cosh(f) - (a / 3)
            x2 = sqrt(q) * cosh(f) - (a / 3) + 1j * sqrt(3) * sqrt(q) * sinh(f)
            x3 = sqrt(q) * cosh(f) + (a / 3) + 1j * sqrt(3) * sqrt(q) * sinh(f)
            print("x1 = ", round(x1))
            print("x2 = ", round(x2))
            print("x3 = ", round(x3))
            res = str(round(x1)) + " " + str(round(x2)) + " " + str(round(x3))
        elif r == 0:
            x1 = -a / 3
            x2 = (-a / 3) - 1j * sqrt(3) * sqrt(q) * sinh(f)
            x3 = (-a / 3) + 1j * sqrt(3) * sqrt(q) * sinh(f)
            print("x1 = ", round(x1))
            print("x2 = ", round(x2))
            print("x3 = ", round(x3))
            res = str(round(x1)) + " " + str(round(x2)) + " " + str(round(x3))
        else:
            x1 = 2 * sqrt(q) * cosh(f) - a / 3
            x2 = -1 * sqrt(q) * cosh(f) - a / 3 + 1j * sqrt(3) * sqrt(q) * sinh(f)
            x3 = -1 * sqrt(q) * cosh(f) - a / 3 - 1j * sqrt(3) * sqrt(q) * sinh(f)
            print("x1 = ", round(x1))
            print("x2 = ", round(x2))
            print("x3 = ", round(x3))
            res = str(round(x1)) + " " + str(round(x2)) + " " + str(round(x3))
    elif q < 0:
        from cmath import asinh, cosh, sinh, sqrt
        f = (1 / 3) * asinh(abs(r) / sqrt(q**3))
        if r > 0:
            x1 = -2 * sqrt(abs(q)) * sinh(f) - a / 3
            x2 = sqrt(abs(q)) * sinh(f) - a / 3  + 1j * sqrt(3) * sqrt(abs(q)) * cosh(f)
            x3 = sqrt(abs(q)) * sinh(f) - a / 3  - 1j * sqrt(3) * sqrt(abs(q)) * cosh(f)
            print("x1 = ", round(x1))
            print("x2 = ", round(x2))
            print("x3 = ", round(x3))
            res = str(round(x1)) + " " + str(round(x2)) + " " + str(round(x3))
        elif r == 0:
            x1 = -a / 3
            x2 = -a / 3 + 1j * sqrt(3) * sqrt(abs(q)) * cosh(f)
            x3 = -a / 3 - 1j * sqrt(3) * sqrt(abs(q)) * cosh(f)
            print("x1 = ", round(x1))
            print("x2 = ", round(x2))
            print("x3 = ", round(x3))
            res = str(round(x1)) + " " + str(round(x2)) + " " + str(round(x3))
        else:
            x1 = 2 * sqrt(abs(q)) * sinh(f) - a / 3
            x2 = -1 * sqrt(abs(q)) * sinh(f) - a / 3 + 1j * sqrt(3) * cosh(f)
            x3 = -1 * sqrt(abs(q)) * sinh(f) + a / 3 + 1j * sqrt(3) * cosh(f)
            print("x1 = ", round(x1))
            print("x2 = ", round(x2))
            print("x3 = ", round(x3))
            res = str(round(x1)) + " " + str(round(x2)) + " " + str(round(x3))
    else:
        from cmath import sqrt
        x1 = -((c - (a * 3) / 27))**(1 / 3) - a / 3
        x2 = (-a + x1) / 2 + 1j / 2 * sqrt(abs((a - 3 * x1) * (a + x1) - 4 * b))
        x3 = x2 = (-a + x1) / 2 - 1j / 2 * sqrt(abs((a - 3 * x1) * (a + x1) - 4 * b))
        print("x1 = ", round(x1))
        print("x2 = ", round(x2))
        print("x3 = ", round(x3))
        res = str(round(x1)) + " " + str(round(x2)) + " " + str(round(x3))
else:
    x1 = -2 * (r)**(1 / 3) - a / 3
    x2 = (r)**(1 / 3) - a / 3
    print("x1 = ", round(x1))
    print("x2 = ", round(x2))
    res = str(round(x1)) + " " + str(round(x2))

output.write(res) #виведення результату
input.close() #закриття файлу з вхідними даними
output.close() #закриття файлу з результатом
# Дяченко В.В, ЗПІ-18
# Написати програму, що розраховує мінімум, на скільки шматочків потрібно розрізати пиріг
# (інакше повбивають один одного...)

a = int(input("біологи: "))  # кількість учасників в команді біологів
b = int(input("інформатики: "))  # кількість учасників в команді інформатиків

pie_a = a
pie_b = b

while pie_a != pie_b:  # доки к-ть шматочків не рівна, повторювати наступний алгоритм:
    if pie_a > pie_b:  # якщо в біологів більше (ГМО застосували)...
        pie_b += b  # збільшити для інформатиків
    else:
        pie_a += a  # і навпаки. Доки не зрівняються

print('Пиріг треба поділити на', pie_a,
      'рівних частин')  # вивести результат

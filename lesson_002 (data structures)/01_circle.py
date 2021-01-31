# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
pi = 3.1415926
square = pi * radius ** 2
print(round(square, 4))

# Далее, пусть есть координаты точки
point = (23, 34)
# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
hypotenuse = (point[0] ** 2 + point[1] ** 2) ** .5
if hypotenuse <= radius:
    print(True)
else:
    print(False)
# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
hypotenuse_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** .5
if hypotenuse_2 <= radius:
    print(True)
else:
    print(False)

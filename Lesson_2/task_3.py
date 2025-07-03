import math

def square(side):
    area = side ** 2
    return math.ceil(area)

side = float(input("Введите сторону квадрата: "))
print(square(side))


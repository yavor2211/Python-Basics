# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle или triangle).
# •	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# •	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# •	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# •	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.
import math

figure=input()

if figure=="square":
    side_a=float(input())
    area=side_a*side_a
elif figure=="rectangle":
    side_a=float(input())
    side_b=float(input())
    area=side_b*side_a
elif figure=="circle":
    radius=float(input())
    area=math.pi*radius*radius
# elif figure=="triangle":
else:
    side_a=float(input())
    h_a=float(input())
    area=side_a*h_a/2

print(f"{area : .3f}")
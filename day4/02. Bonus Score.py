# Дадено е цяло число – начален брой точки.
number_up_to_100=100
number_up_to_1000=1000
five_bonus_points=5
ten_percent=0.10
twenty_percent=0.20
even_number_points=1
finish_five_points=2
# Върху него се начисляват бонус точки по правилата, описани по-долу.
# Да се напише програма, която пресмята бонус точките, които получава числото и общия брой точки (числото + бонуса).
# •	Ако числото е до 100 включително, бонус точките са 5;
# •	Ако числото е по-голямо от 100, бонус точките са 20% от числото;
# •	Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
#
# •	Допълнителни бонус точки (начисляват се отделно от предходните):
# o	За четно число  + 1 т.
# o	За число, което завършва на 5  + 2 т.
bonus_points=0
number=int(input())

if number <=100:
    bonus_points+=5
elif number >1000:
    bonus_points+=(number*ten_percent)
else:
    bonus_points += (number * twenty_percent)

if number % 2 ==0:
    bonus_points+=even_number_points
elif number % 10 ==5:
    bonus_points+=finish_five_points

print(bonus_points)
print(bonus_points+number)
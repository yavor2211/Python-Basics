ROSE = 5
DAHLIAS = 3.80
TULIPS = 2.80
NARCISSUS = 3
GLADIOLUS = 2.50

flowers = input()
number_of_flowers = int(input())
budget = int(input())
Rose_discount = 0.10
Dahlias_discount = 0.15
Tulips_discount = 0.15
Narcissus_increase = 0.15
Gladiolus_increase = 0.20
price_flowers = 0

if flowers =='Roses':
    price_flowers+=ROSE*number_of_flowers
    if number_of_flowers > 80:
        price_flowers -=price_flowers*Rose_discount

elif flowers == 'Dahlias':
    price_flowers+=DAHLIAS*number_of_flowers
    if number_of_flowers > 90:
        price_flowers-=price_flowers*Dahlias_discount

elif flowers == 'Tulips':
    price_flowers+=TULIPS*number_of_flowers
    if number_of_flowers >80:
        price_flowers-=price_flowers*Tulips_discount
elif flowers == 'Narcissus':
    price_flowers+=NARCISSUS*number_of_flowers
    if number_of_flowers <120:
        price_flowers+=price_flowers*Narcissus_increase
elif flowers == 'Gladiolus':
    price_flowers+=GLADIOLUS*number_of_flowers
    if number_of_flowers <80:
        price_flowers+=price_flowers*Gladiolus_increase

if budget >= price_flowers:
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers} and {budget-price_flowers:.2f} leva left.")
else:
    print(f"Not enough money, you need {price_flowers-budget:.2f} leva more.")
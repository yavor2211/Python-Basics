import math
beer_price=1.20

football_fan=input()
budget=float(input())
count_bottles_beer=int(input())
count_packages_chips=int(input())

total_beer_price=beer_price*count_bottles_beer
packet_chips_price=total_beer_price*0.45
total_chips_price=math.ceil(packet_chips_price*count_packages_chips)

total_price=total_chips_price+total_beer_price

if budget >= total_price:
    print(f'{football_fan} bought a snack and has {budget-total_price:.2f} leva left.')
else:
    print(f'{football_fan} needs {total_price-budget:.2f} more leva!')
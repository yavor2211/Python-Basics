import math
tennis_racket_price = float(input())
tennis_racket_quantity = int(input())
sneakers_quantity = int(input())
sneaker_price = tennis_racket_price / 6

other_equipment_price =0.20

total_price_rackets = tennis_racket_price * tennis_racket_quantity
total_price_sneakers = sneaker_price * sneakers_quantity

total_price_other_equipment=(total_price_sneakers+total_price_rackets) * other_equipment_price

total_price_everything=total_price_other_equipment+total_price_rackets+total_price_sneakers

total_price_player=math.floor(total_price_everything/8)

total_price_sponsors=math.ceil(total_price_everything*7/8)

print(f'Price to be paid by Djokovic {total_price_player}')
print(f'Price to be paid by sponsors {total_price_sponsors}')


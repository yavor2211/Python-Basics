SPRING_PRICE=3000
SUMMER_PRICE=4200
AUTUMN_PRICE=4200
WINTER_PRICE=2600
THRESHOLD_SIX=6
THRESHOLD_SEVEN=7
THRESHOLD_ELEVEN=11
THRESHOLD_TWELVE=12
budget = int(input())
season = input()
fishermen = int(input())
price = 0
discount_five_percent=0.05   # if is spring, summer or winter
discount_ten_percent=0.10   # up to =6
discount_fifteen_percent=0.15   # from 7 to =11
discount_twenty_five_percent: float=0.25   # from 12+

if season == 'Spring':
    price+=SPRING_PRICE
    if fishermen <= THRESHOLD_SIX:
        price -= (price * discount_ten_percent)
    elif fishermen > THRESHOLD_SEVEN and fishermen <= THRESHOLD_ELEVEN:
        price -= (price * discount_fifteen_percent)
    elif fishermen >= THRESHOLD_TWELVE:
        price -= (price * discount_twenty_five_percent)
elif season == 'Summer':
    price+=SUMMER_PRICE
    if fishermen <= THRESHOLD_SIX:
        price -= (price * discount_ten_percent)
    elif fishermen > THRESHOLD_SEVEN and fishermen <= THRESHOLD_ELEVEN:
        price -= (price * discount_fifteen_percent)
    elif fishermen >= THRESHOLD_TWELVE:
        price -= (price * discount_twenty_five_percent)
elif season == 'Autumn':
    price+=SUMMER_PRICE
    if fishermen <= THRESHOLD_SIX:
        price -= (price * discount_ten_percent)
    elif fishermen > THRESHOLD_SEVEN and fishermen <= THRESHOLD_ELEVEN:
        price -= (price * discount_fifteen_percent)
    elif fishermen >= THRESHOLD_TWELVE:
        price -=(price * discount_twenty_five_percent)
else:
    price+=WINTER_PRICE
    if fishermen <= THRESHOLD_SIX:
        price -= (price * discount_ten_percent)
    elif THRESHOLD_SEVEN < fishermen and fishermen <= THRESHOLD_ELEVEN:
        price -= (price * discount_fifteen_percent)
    elif fishermen >= THRESHOLD_TWELVE:
        price = price - (price * discount_twenty_five_percent)

if season != 'Autumn' and fishermen % 2 ==0:
    price-=(price*discount_five_percent)

if budget >= price:
    print(f"Yes! You have {budget-price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price-budget:.2f} leva.")

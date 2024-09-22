budget=float(input())
season=input()

DESTINATION_ONE='Bulgaria'
DESTINATION_TWO='Europe'
DESTINATION_THREE='Balkans'
THRESHOLD_HUNDRED=100
THRESHOLD_THOUSAND=1000
TYPE_OF_DESTINATION_ONE='Hotel'
TYPE_OF_DESTINATION_TWO='Camp'
price = 0
place=''
place_for_break=''
thirty_percent_of_budget=0.30
seventy_percent_of_budget=0.70
forty_percent_of_budget=0.40
eighty_percent_of_budget=0.80
ninety_percent_of_budget=0.90

if season == 'summer':
    if budget <=THRESHOLD_HUNDRED:
        place=DESTINATION_ONE
        price+=(budget*thirty_percent_of_budget)
        place_for_break=TYPE_OF_DESTINATION_TWO

    elif budget <= THRESHOLD_THOUSAND:
        place=DESTINATION_THREE
        price+=(budget*forty_percent_of_budget)
        place_for_break = TYPE_OF_DESTINATION_TWO
    else:
        place=DESTINATION_TWO
        price+=(budget*ninety_percent_of_budget)
        place_for_break = TYPE_OF_DESTINATION_ONE


elif season == 'winter':
    if budget <= THRESHOLD_HUNDRED:
        place = DESTINATION_ONE
        price += (budget * seventy_percent_of_budget)
        place_for_break = TYPE_OF_DESTINATION_ONE

    elif budget <= THRESHOLD_THOUSAND:
        place = DESTINATION_THREE
        price += (budget * eighty_percent_of_budget)
        place_for_break = TYPE_OF_DESTINATION_ONE

    else:
        place = DESTINATION_TWO
        price += (budget * ninety_percent_of_budget)
        place_for_break = TYPE_OF_DESTINATION_ONE

print(f'Somewhere in {place}')
print(f'{place_for_break} - {price:.2f}')
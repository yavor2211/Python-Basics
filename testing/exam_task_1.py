NIGHT_PRICE=20
CARD_FOR_TRANSPORT=1.60
MUSEUM_TICKET=6
ADDITIONAL_PERCENTAGE=1-0.75

quantity_people_group=int(input())
quantity_nights=int(input())
quantity_cards_for_transport=int(input())
quantity_museum_tickets=int(input())


price_for_nights=quantity_nights*NIGHT_PRICE
price_cards_for_transport=quantity_cards_for_transport*CARD_FOR_TRANSPORT
price_tickets_for_museum=quantity_museum_tickets*MUSEUM_TICKET
price_for_one_person=price_for_nights+price_cards_for_transport+price_tickets_for_museum

total_price=price_for_one_person*quantity_people_group
total_price_addition=total_price+(total_price*ADDITIONAL_PERCENTAGE)

print(f'{total_price_addition:.2f}')
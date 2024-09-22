import math
video_cards=13
extensions=13
second_hand_price=1000

price_video_card=int(input())
price_extension=int(input())
electricity_card_day=float(input())
winning_card_day=float(input())

total_price_card=video_cards*price_video_card
total_price_extension=extensions*price_extension
total_price=total_price_extension+total_price_card+second_hand_price

winning_for_day_card=winning_card_day-electricity_card_day

total_winning_day_cards=video_cards*winning_for_day_card

days_for_investing=total_price/total_winning_day_cards
total_days=math.ceil(days_for_investing)

print(f'{total_price}\n{total_days}')
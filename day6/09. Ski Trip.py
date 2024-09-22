ROOM = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35
DISCOUNT_APA_30 = 0.30
DISCOUNT_APA_35 = 0.35
DISCOUNT_APA_50 = 0.50
DISCOUNT_PR_APA_10 = 0.10
DISCOUNT_PR_APA_15 = 0.15
DISCOUNT_PR_APA_20 = 0.20
POSITIVE_ADDITION = 0.25
NEGATIVE_DECREASE = 0.10
THRESHOLD_FOR_DISCOUNT_10 = 10
THRESHOLD_FOR_DISCOUNT_15 = 15

days_staying = int(input()) - 1
type_of_property = input()
score_given = input()
price = 0

if type_of_property == 'apartment':
    price += (days_staying * APARTMENT)
    if days_staying < THRESHOLD_FOR_DISCOUNT_10:
        price -= (price * DISCOUNT_APA_30)
    elif THRESHOLD_FOR_DISCOUNT_10 <= days_staying <= THRESHOLD_FOR_DISCOUNT_15:
        price -= (price * DISCOUNT_APA_35)
    elif days_staying > THRESHOLD_FOR_DISCOUNT_15:
        price -= (price * DISCOUNT_APA_50)
elif type_of_property == 'president apartment':
    price += (days_staying * PRESIDENT_APARTMENT)
    if days_staying < THRESHOLD_FOR_DISCOUNT_10:
        price -= (price * DISCOUNT_PR_APA_10)
    elif THRESHOLD_FOR_DISCOUNT_10 <= days_staying <= THRESHOLD_FOR_DISCOUNT_15:
        price -= (price * DISCOUNT_PR_APA_15)
    elif days_staying > THRESHOLD_FOR_DISCOUNT_15:
        price -= (price * DISCOUNT_PR_APA_20)
else:
    price += (days_staying * ROOM)

if score_given == 'positive':
    price += (price * POSITIVE_ADDITION)
else:
    price -= (price * NEGATIVE_DECREASE)

print(f'{price:.2f}')

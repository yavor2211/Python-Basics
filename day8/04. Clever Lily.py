MONEY_FOR_EVEN_BIRTHDAY = 10
MONEY_STOLEN_BROTHER = 1

age_of_lily = int(input())
price_washing_machine = float(input())
price_toy = int(input())

count_toys = 0
money_start = 10
total_money = 0
result = ''
for years in range(1, age_of_lily + 1):

    if years % 2 == 0:
        total_money += money_start - MONEY_STOLEN_BROTHER
        money_start += MONEY_FOR_EVEN_BIRTHDAY

    else:
        count_toys += 1

total_money += (count_toys * price_toy)

if total_money >= price_washing_machine:
    result = f'Yes! {abs(price_washing_machine - total_money):.2f}'
else:
    result = f'No! {abs(total_money - price_washing_machine):.2f}'

print(result)

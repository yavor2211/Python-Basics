football_team = input()
souvenirs = input()
amount_souvenirs = int(input())
price = 0
if football_team == 'Argentina' and souvenirs == 'flags':
    price = 3.25
elif football_team == 'Argentina' and souvenirs == 'caps':
    price = 7.20
elif football_team == 'Argentina' and souvenirs == 'posters':
    price = 5.10
elif football_team == 'Argentina' and souvenirs == 'stickers':
    price = 1.25

elif football_team == 'Brazil' and souvenirs == 'flags':
    price = 4.20
elif football_team == 'Brazil' and souvenirs == 'caps':
    price = 8.50
elif football_team == 'Brazil' and souvenirs == 'posters':
    price = 5.35
elif football_team == 'Brazil' and souvenirs == 'stickers':
    price = 1.20

elif football_team == 'Croatia' and souvenirs == 'flags':
    price = 2.75
elif football_team == 'Croatia' and souvenirs == 'caps':
    price = 6.90
elif football_team == 'Croatia' and souvenirs == 'posters':
    price = 4.95
elif football_team == 'Croatia' and souvenirs == 'stickers':
    price = 1.10
elif football_team == 'Denmark' and souvenirs == 'flags':
    price = 3.10
elif football_team == 'Denmark' and souvenirs == 'caps':
    price = 6.50
elif football_team == 'Denmark' and souvenirs == 'posters':
    price = 4.80
elif football_team == 'Denmark' and souvenirs == 'stickers':
    price = 0.90

total_price = price * amount_souvenirs

if football_team != 'Argentina' and football_team != 'Brazil' and football_team != 'Croatia' and football_team != 'Denmark':
    print(f'Invalid country!')
elif souvenirs != 'flags' and souvenirs != 'caps' and souvenirs != 'posters' and souvenirs != 'stickers':
    print(f'Invalid stock!')
else:
    print(f'Pepi bought {amount_souvenirs} {souvenirs} of {football_team} for {total_price:.2f} lv.')

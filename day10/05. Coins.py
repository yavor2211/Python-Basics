COINS_2_LEVA=200
COINS_1_LEV=100
COINS_50_ST=50
COINS_20_ST=20
COINS_10_ST=10
COINS_5_ST=5
COINS_2_ST=2
COINS_1_ST=1

change = int(float(input())*100)
count_coins=0

while change > 0:

    if change >= COINS_2_LEVA:
        change-=COINS_2_LEVA
    elif change >= COINS_1_LEV:
        change-=COINS_1_LEV
    elif change >= COINS_50_ST:
        change-=COINS_50_ST
    elif change >=COINS_20_ST:
        change-=COINS_20_ST
    elif change >= COINS_10_ST:
        change-=COINS_10_ST
    elif change>= COINS_5_ST:
        change-=COINS_5_ST
    elif change >= COINS_2_ST:
        change-=COINS_2_ST
    elif change>=COINS_1_ST:
        change-=COINS_1_ST
    count_coins+=1

print(count_coins)
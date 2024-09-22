kilo_food_price = 12.45
THRESHOLD_100 = 100
THRESHOLD_200 = 200
THRESHOLD_300 = 300
THRESHOLD_400 = 400

count_cats_first_group = 0
count_cats_second_group = 0
count_cats_third_group = 0
total_food_cats = 0

total_cats = int(input())
for _ in range(total_cats):
    food_for_cat = float(input())

    if THRESHOLD_100 <= food_for_cat < THRESHOLD_200:
        count_cats_first_group += 1
        total_food_cats += food_for_cat

    elif THRESHOLD_200 <= food_for_cat < THRESHOLD_300:
        count_cats_second_group += 1
        total_food_cats += food_for_cat

    elif THRESHOLD_300 <= food_for_cat < THRESHOLD_400:
        count_cats_third_group += 1
        total_food_cats += food_for_cat

kilogram_food = total_food_cats / 1000
price_food = f'{kilo_food_price * kilogram_food:.2f}'
print(f'Group 1: {count_cats_first_group} cats.')
print(f'Group 2: {count_cats_second_group} cats.')
print(f'Group 3: {count_cats_third_group} cats.')
print(f'Price for food per day: {price_food} lv.')

import math

count_days_missing = int(input())
left_food_in_kilos = int(input())
food_for_day_first_reindeer = float(input())
food_for_day_second_reindeer = float(input())
food_for_day_third_reindeer = float(input())

needed_food_first_reindeer = count_days_missing * food_for_day_first_reindeer
needed_food_second_reindeer = count_days_missing * food_for_day_second_reindeer
needed_food_third_reindeer = count_days_missing * food_for_day_third_reindeer

total_amount_food_needed = needed_food_first_reindeer + needed_food_second_reindeer + needed_food_third_reindeer

food_left = math.floor(left_food_in_kilos - total_amount_food_needed)

food_needed_more = math.ceil(total_amount_food_needed - left_food_in_kilos)

if total_amount_food_needed < left_food_in_kilos:
    print(f'{food_left} kilos of food left.')
else:
    print(f'{food_needed_more} more kilos of food are needed.')

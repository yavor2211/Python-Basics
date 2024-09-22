amount_locations = int(input())
total_gold_for_day = 0
result = ''
for location in range(amount_locations):
    average_gold_per_day = float(input())
    amount_days = int(input())
    average_gold_drilled=0
    total_gold_for_day=0
    for day in range(amount_days):
        gold_for_day = float(input())
        total_gold_for_day += gold_for_day
        average_gold_drilled = total_gold_for_day / amount_days

    if average_gold_drilled >= average_gold_per_day:
        print(f'Good job! Average gold per day: {average_gold_drilled:.2f}.')
    elif average_gold_drilled < average_gold_per_day:
        print(f'You need {abs(average_gold_drilled - average_gold_per_day):.2f} gold.')


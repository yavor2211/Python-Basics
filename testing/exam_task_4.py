import math

THRESHOLD_KILOMETERS = 1_000

number_of_days = int(input())
amount_kilometers_run_first_day = float(input())
total_kilometers = 0
# result = ''

for day in range(1, number_of_days + 1):
    percentage_increase_norm = int(input()) / 100
    total_kilometers += amount_kilometers_run_first_day
    amount_kilometers_run_first_day += (amount_kilometers_run_first_day * percentage_increase_norm)

total_kilometers += amount_kilometers_run_first_day
total_kilometers_more = math.ceil(THRESHOLD_KILOMETERS - total_kilometers)
total_kilometers_less = math.ceil(total_kilometers - THRESHOLD_KILOMETERS)

if total_kilometers >= THRESHOLD_KILOMETERS:
    print(f"You've done a great job running {abs(total_kilometers_less)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {total_kilometers_more} more kilometers")

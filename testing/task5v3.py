base_camp = 5364
mountain_peak = 8848
allowed_days = 5
is_got_on_top = False
command = input()
meters_hiked = int(input())
count_days = 0
count_meters_per_day = 0
total_meters=0
while True:
    if command == 'Yes':

        count_days += 1
    elif command == 'No':
        continue

    count_meters_per_day += meters_hiked
    total_meters +=meters_hiked
    if meters_hiked >= mountain_peak:
        print(f'Goal reached for {count_days} days!')
        is_got_on_top = True
        break
    elif count_days > allowed_days:
        print(f'Failed!\n{total_meters}')

        break
    elif command == 'END':
        print(f'Failed!\n{total_meters}')
        break
    if is_got_on_top:
        break

total_meters+=base_camp
print(total_meters)
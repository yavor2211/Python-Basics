base_camp = 5364
mountain_peak = 8848
allowed_days=5
is_got_on_top = False
command = input()
meters_hiked = int(input())
count_days = 0
count_meters_per_day=0
total_meters_hiked=0
result=''
while True:
    if command == 'Yes':

        count_days += 1
    elif command == 'No':
        continue

    total_meters_hiked+=meters_hiked

    if (base_camp+total_meters_hiked) >= mountain_peak:
        result=f'Goal reached for {count_days} days!'
        is_got_on_top=True
        break
    elif count_days>=allowed_days:
        result=f'Failed!\n{base_camp+total_meters_hiked}'
        break
    elif command =='END':
        result=f'Failed!\n{base_camp+meters_hiked}'
        break

    if is_got_on_top:
        break
    count_days+=1
print(result)
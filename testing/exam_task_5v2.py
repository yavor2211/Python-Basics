base_camp = 5364
mountain_peak = 8848

count_days = 1
allowed_days = 5
total_meters_hiked = 0
command = input()
result = ''
while command != 'END':
    hiked_meters=int(input())
    total_meters_hiked += hiked_meters
    base_camp += total_meters_hiked

    if command == 'Yes':
        count_days+=1
        if count_days>allowed_days:
            print(f'Failed!\n{base_camp}')
            break
        base_camp+=hiked_meters

    else:
        base_camp+=hiked_meters

    if base_camp>=mountain_peak:
        print(f'Goal reached for {count_days} days!')
        break
    count_days+=1
    command=input()

if command =='END':
    if base_camp >= mountain_peak:
        print(f'Goal reached for{count_days} days!')
    else:
        print(f'Failed!\n{base_camp}')

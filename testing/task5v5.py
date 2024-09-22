base_camp=5364
mountain_peak=8848


command=input()
meters_hiked=int(input())
count_days=0
total_meters_hiked=0
allowed_days=5
while True:
    base_camp+=meters_hiked

    if command =='Yes':
        count_days+=1

    elif command == 'No':
        continue

    elif command =='END':
        print(f'Failed!\n{base_camp}')
        break

    if base_camp>mountain_peak:
        print(f'Goal reached for {count_days} days.')
    elif count_days>allowed_days:
        print(f'Failed!\n{base_camp}')
        break

    count_days+=1


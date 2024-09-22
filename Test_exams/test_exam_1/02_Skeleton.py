minutes_in_control = int(input())
seconds_in_control = int(input())
length_in_meters = float(input())
seconds_for_100_meters = int(input())
time_lost_per_120_meters = 2.5
result = ''
total_time_in_control = (minutes_in_control * 60) + seconds_in_control

time_lost_for_meters = length_in_meters / 120

time_lost_in_seconds = time_lost_for_meters * time_lost_per_120_meters

time_of_marin = (length_in_meters / 100) *int(time_lost_for_meters) - time_lost_in_seconds

if time_of_marin < total_time_in_control:
    result = f'Marin Bangiev won an Olympic quota!\nHis time is {time_of_marin:.3f}.'

else:
    result = f'No, Marin failed! He was {abs(time_of_marin - total_time_in_control):.3f} second slower.'

print(result)

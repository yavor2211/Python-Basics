import math


name=input()
length_of_movie=int(input()А
time_of_break=int(input())
time_for_lunch=time_of_break/8
time_for_rest=time_of_break/4
total_time=time_for_rest+time_for_lunch+length_of_movie
time_left=time_of_break-(time_for_lunch+time_for_rest)

if time_left>=length_of_movie:
    print(f"You have enough time to watch {name} and left with {math.ceil(time_of_break-total_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(length_of_movie-time_left)} more minutes.")
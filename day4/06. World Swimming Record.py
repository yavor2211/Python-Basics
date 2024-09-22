
# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди
# Да се изчисли времето в секунди, за което Иванчо ще преплува разстоянието и разликата спрямо Световния рекорд.
ADDITIONAL_METERS=15
ADDITIONAL_SECONDS=12.5



record_in_seconds=float(input())
distance_in_meters=float(input())
time_in_seconds_for_meter=float(input())


distance_needed_to_swim=time_in_seconds_for_meter*distance_in_meters
space_lost=distance_in_meters//ADDITIONAL_METERS
time_lost=space_lost*ADDITIONAL_SECONDS

total_time=time_lost+distance_needed_to_swim
if total_time<record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:0.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time-record_in_seconds:0.2f} seconds slower.")

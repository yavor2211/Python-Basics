MINUTES_IN_HOUR = 60

hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_minutes = hour_of_exam * MINUTES_IN_HOUR + minute_of_exam
arrival_minutes = hour_of_arrival * MINUTES_IN_HOUR + minute_of_arrival

time_diff = exam_minutes - arrival_minutes
print_text = ''
if time_diff > 30:
    print_text = 'Early'
elif time_diff < 0:
    print_text = 'Late'
else:
    print_text = 'On time'

result = ''

hours = abs(time_diff) // MINUTES_IN_HOUR
minutes = abs(time_diff) % MINUTES_IN_HOUR

if hours > 0:
    result += f'{hours} : {minutes:02d} hours'
elif minutes > 0:
    result += f'{minutes} minutes'

if time_diff > 0:
    result += ' before the start'
elif time_diff < 0:
    result += ' after the start'

print(print_text)
print(result)

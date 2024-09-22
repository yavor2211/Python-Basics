# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.
# Ако денят е работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend".
# Ако се въведе текст различен от ден от седмицата да се отпечата - "Error".
DAY_OF_WEEK = input()

if (DAY_OF_WEEK == 'Monday'
        or DAY_OF_WEEK == 'Tuesday'
        or DAY_OF_WEEK == 'Wednesday'
        or DAY_OF_WEEK == 'Thursday'
        or DAY_OF_WEEK == 'Friday'):
    print('Working day')
elif DAY_OF_WEEK == 'Saturday' or DAY_OF_WEEK == 'Sunday':
    print('Weekend')
else:
    print('Error')
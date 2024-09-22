NUMBER_OF_DAY = int(input())
result = ''
if NUMBER_OF_DAY == 1:
    result = 'Monday'
elif NUMBER_OF_DAY == 2:
    result = 'Tuesday'
elif NUMBER_OF_DAY == 3:
    result = 'Wednesday'
elif NUMBER_OF_DAY == 4:
    result = 'Thursday'
elif NUMBER_OF_DAY == 5:
    result = 'Friday'
elif NUMBER_OF_DAY == 6:
    result = 'Saturday'
elif NUMBER_OF_DAY == 7:
    result = 'Sunday'
else:
    print('Error')

print (result)

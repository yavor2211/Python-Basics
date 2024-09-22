HOUR_OF_THE_DAY=int(input())
DAY_OF_THE_WEEK= input()
# и проверява дали офисът на фирма е отворен,

# като работното време на офисът е от 10-18 часа, от понеделник до събота включително

if HOUR_OF_THE_DAY >= 10 and HOUR_OF_THE_DAY <= 18:
    if DAY_OF_THE_WEEK == 'Monday':
        print('open')
    elif DAY_OF_THE_WEEK == 'Tuesday':
        print('open')
    elif DAY_OF_THE_WEEK == 'Wednesday':
        print('open')
    elif DAY_OF_THE_WEEK == 'Thursday':
        print('open')
    elif DAY_OF_THE_WEEK == 'Friday':
        print('open')
    elif DAY_OF_THE_WEEK == 'Saturday':
        print('open')
    else:
        print('closed')
else:
    print('closed')
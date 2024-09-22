AGE = float(input())
GENDER = input()

if GENDER == 'm':
    if AGE < 16:
        print('Master')
    else:
        print('Mr.')
elif GENDER == 'f':
    if AGE < 16:
        print('Miss')
    else:
        print('Ms.')

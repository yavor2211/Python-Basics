number=int(input())

for num in range(1111, 9999+1):
    for digit in str(num):
        if digit =='0':
            break
        if number % int(digit) !=0:
            break

    else:
            print(num, end=' ')
number_one = int(input())
number_two = int(input())

for number in range(number_one, number_two + 1):
    even_sum = 0
    odd_sum = 0
    for idx, digit in enumerate(str(number)):

        digit = int(digit)

        if idx % 2 == 0:
            even_sum += digit

        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(number, end=' ')

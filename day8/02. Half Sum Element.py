n = int(input())

max_num = float('-inf')
sum_numbers = 0

for _ in range(n):
    number = int(input())

    if number > max_num:
        max_num = number

    sum_numbers += number

half_sum = sum_numbers - max_num
result = ''

if max_num == half_sum:
    result = f'Yes\nSum = {max_num}'
else:
    result = f'No\nDiff = {abs(max_num - half_sum)}'

print(result)

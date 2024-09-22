# Да се напише програма, която чете 2 * n-на брой цели числа,
# подадени от потребителя,
# и проверява дали сумата на първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума).
# При равенство печата " Yes, sum = " + сумата; иначе печата " No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

n = int(input())
left_sum = 0
right_sum = 0

for _ in range(n):
    current_number=int(input())
    left_sum+=current_number

for _ in range(n):
    current_number=int(input())
    right_sum+=current_number

if left_sum == right_sum :
    print(f'Yes, sum = {left_sum}')
else:
    difference=abs(left_sum-right_sum)
    print(f'No, diff = {difference}')


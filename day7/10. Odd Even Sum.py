# Да се напише програма, която чете n-на брой цели числа,
# подадени от потребителя и проверява дали сумата от числата на четни позиции
# е равна на сумата на числата на нечетни позиции.
# •	Ако сумите са равни да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;
# •	Ако сумите не са равни да се отпечат два реда: "No" и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.

n = int(input())
odd_sum=0
even_sum=0

for _ in range(1,n+1):
    current_number=int(input())

    if _ % 2 ==0:
        even_sum+=current_number
    else:
        odd_sum+=current_number

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    print(f'Diff = {abs(even_sum-odd_sum)}')
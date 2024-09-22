# Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа.
# На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число.
# Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.
first_number = int(input())
second_number = int(input())
magic_number = int(input())
combination = 0
should_break=False
for x in range(first_number,second_number+1):

    for y in range(first_number,second_number+1):
        combination+=1
        if x + y == magic_number:
            print(f'Combination N:{combination} ({x} + {y} = {magic_number})')
            should_break=True

    if should_break:
        break
else:
    print(f'{combination} combinations - neither equals {magic_number}')

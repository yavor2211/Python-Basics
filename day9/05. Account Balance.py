total_sum = 0

result = ''

payments = input()
while payments != 'NoMoreMoney':
    current_number = float(payments)
    if current_number < 0:
        print(f'Invalid operation!')
        break
    print(f'Increase: {current_number:.2f}')
    total_sum += current_number
    payments = input()

print(f'Total: {total_sum:.2f}')

MONEY_LEFT_AFTER_SPENDING_EVERYTHING = 0
threshold_days_spending = 5

needed_money_vacation = float(input())
money_having_now = float(input())

days_spending_count = 0
total_days_count = 0
result = ''

while days_spending_count < threshold_days_spending:
    type_of_action = input()
    sum_of_using = float(input())
    total_days_count += 1

    if type_of_action == 'spend':
        money_having_now = money_having_now - sum_of_using if money_having_now > 0 else 0
        days_spending_count += 1


    elif type_of_action == 'save':
        money_having_now += sum_of_using
        days_spending_count = 0

        if money_having_now >= needed_money_vacation:
            result = f'You saved the money for {total_days_count} days.'
            break

else:

    result = f"You can't save the money.\n{total_days_count}"
print(result)

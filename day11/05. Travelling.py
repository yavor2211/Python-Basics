command = input()
while command != 'End':
    destination = command
    budget_needed = float(input())

    total_saving = 0
    while total_saving < budget_needed:
        money_saving_up = float(input())

        total_saving += money_saving_up

    print(f'Going to {destination}!')

    command = input()

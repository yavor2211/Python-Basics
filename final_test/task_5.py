food_bought_in_kg = int(input())
command = input()
result = ''
amount_food = 0
food_in_grams = food_bought_in_kg * 1000
while command != 'Adopted':
    food_eaten = int(command)
    amount_food += food_eaten
    if amount_food > food_in_grams:
        result = f'Food is not enough. You need {amount_food - food_in_grams} grams more.'

    elif amount_food <= food_in_grams:
        result = f'Food is enough! Leftovers: {food_in_grams - amount_food} grams.'

    command = input()
print(result)
space_taken = 0
empty_space = int(input()) * int(input()) * int(input())
result = ''

while space_taken < empty_space:
    boxes = input()

    if boxes == 'Done':
        result = f'{empty_space - space_taken} Cubic meters left.'
        break

    space_taken += int(boxes)
else:
    result = f'No more free space! You need {space_taken - empty_space} Cubic meters more.'
print(result)

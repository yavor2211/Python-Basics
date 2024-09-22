size_cake = int(input()) * int(input())

count_pieces = 0
result = ''
while size_cake > count_pieces:
    pieces = input()

    if pieces == 'STOP':
        result = f'{size_cake - count_pieces} pieces are left. '

        break
    count_pieces += int(pieces)

else:
    result = f'No more cake left! You need {count_pieces - size_cake} pieces more.'

print(result)

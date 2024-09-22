number=int(input())

counter = 0

is_max_number=False
for row in range(1,number+1):
    for column in range(1,row+1):
        counter+=1

        print(counter,end=' ')


        if counter == number:
            is_max_number=True
            break
    if is_max_number:
        break

    print()

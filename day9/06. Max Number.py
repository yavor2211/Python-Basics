import math
import sys

max_number= -sys.maxsize

current_number = 0

command=input()
while command !='Stop':
    value=int(command)

    if value > max_number:
        max_number = value

        current_number+=value


    command = input()
print(max_number)



import math
import sys

min_number= sys.maxsize

current_number = 0

command=input()
while command !='Stop':
    value=int(command)

    if value < min_number:
        min_number = value

        current_number+=value


    command = input()
print(min_number)



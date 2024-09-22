# Напишете програма, която чете n на брой цели числа.
# Принтирайте най-голямото и най-малкото число сред въведените.
import sys

n_numbers = int(input())
min_number = sys.maxsize
max_number = -sys.maxsize

for _ in range(0, n_numbers):
    number = int(input())
    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')

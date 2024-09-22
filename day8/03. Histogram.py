n = int(input())
THRESHOLD_P1 = 200
THRESHOLD_P2 = 400
THRESHOLD_P3 = 600
THRESHOLD_P4 = 800

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

for _ in range(n):
    number = int(input())

    if number < THRESHOLD_P1:
        count_p1 += 1
    elif number < THRESHOLD_P2:
        count_p2 += 1
    elif number < THRESHOLD_P3:
        count_p3 += 1
    elif number < THRESHOLD_P4:
        count_p4 += 1
    else:
        count_p5 += 1


total_count_p = count_p1 + count_p2 + count_p3 + count_p4 + count_p5

percentage_p1 = (count_p1 / n * 100)
percentage_p2 = (count_p2 / n * 100)
percentage_p3 = (count_p3 / n * 100)
percentage_p4 = (count_p4 / n * 100)
percentage_p5 = (count_p5 / n * 100)

print(f'{percentage_p1:.2f}%')
print(f'{percentage_p2:.2f}%')
print(f'{percentage_p3:.2f}%')
print(f'{percentage_p4:.2f}%')
print(f'{percentage_p5:.2f}%')

name_of_student = input()

count_grades = 0
current_class = 1
fails_count = 0

while current_class <= 12:
    yearly_grades = float(input())
    if yearly_grades < 4.00:
        fails_count += 1
        if fails_count >= 2:
            print(f'{name_of_student} has been excluded at {current_class} grade')
            break
        continue

    count_grades += yearly_grades
    current_class += 1

if fails_count < 2:
    average_grade = count_grades / 12
    print(f'{name_of_student} graduated. Average grade: {average_grade:.2f}')

#
# grade = float(input())
# while grade != 2:
#     count_grades+=1
#
#     if grade == '2':
#         print(f'{name_of_student} has been excluded at {} grade')
#         break
#
#
#     grade=float(input())

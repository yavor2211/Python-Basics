count_judges = int(input())

total_sum_grades, total_count_grades = 0, 0
result = ''

while True:
    presentation_name = input()

    if presentation_name == 'Finish':
        break

    sum_current_grades = 0

    for _ in range(count_judges):
        grade = float(input())

        sum_current_grades += grade

    result += f'{presentation_name} - {sum_current_grades / count_judges:.2f}.\n'

    total_sum_grades += sum_current_grades
    total_count_grades += count_judges
result += f"Student's final assessment is {total_sum_grades / total_count_grades:.2f}."
print(result)

failed_threshold=int(input())
GRADE_THRESHOLD=4

failed_times=0
solved_problems_count=0
grades_sum=0
last_problem=''
has_failed=True

while failed_times < failed_threshold:
    problem_name=input()
    if problem_name == 'Enough':
        has_failed=False
        break
    grade = int(input())
    if grade <= GRADE_THRESHOLD:
        failed_times+=1
    grades_sum+=grade
    solved_problems_count+=1
    last_problem=problem_name

if has_failed:
    print(f'You need a break, {failed_times} poor grades.')
else:
    print(f'Average score: {grades_sum/solved_problems_count:.2f}')
    print(f'Number of problems: {solved_problems_count}')
    print(f'Last problem: {last_problem}')

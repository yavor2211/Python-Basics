MINIMUM_POINTS = 1250.5

actor_name = input()
points_from_academy = float(input())
count_judges = int(input())
result = ''
for _ in range(count_judges):
    judge_name = input()
    points_from_judge = float(input())

    points_from_academy += (len(judge_name) * points_from_judge) / 2

    if points_from_academy >= MINIMUM_POINTS:
        result = f'Congratulations, {actor_name} got a nominee for leading role with {points_from_academy:.1f}!'
        break

else:
    result = f'Sorry, {actor_name} you need {MINIMUM_POINTS - points_from_academy:.1f} more!'

print(result)

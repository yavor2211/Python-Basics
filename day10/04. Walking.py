THRESHOLD_STEPS_PER_DAY = 10_000

sum_steps = 0

while sum_steps < THRESHOLD_STEPS_PER_DAY:
    steps_done = input()

    if steps_done == 'Going home':
        steps_home = int(input())
        sum_steps += steps_home
        break
    sum_steps += int(steps_done)

result = ''
if sum_steps >= THRESHOLD_STEPS_PER_DAY:
    result = f'Goal reached! Good job!\n{sum_steps - THRESHOLD_STEPS_PER_DAY} steps over the goal!'
else:
    result = f'{THRESHOLD_STEPS_PER_DAY - sum_steps} more steps to reach goal.'

print(result)

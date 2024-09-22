results=[input().split(':') for result in range(3)]
win=0
lose=0
draw=0

for _ in range(len(results)):

    team_one_goals=int(results[0][0])
    team_two_goals=int(results[0][1])

    if team_one_goals > team_two_goals:
        win+=1

    elif team_one_goals<team_two_goals:
        lose+=1

    elif team_one_goals==team_two_goals:
        draw+=1


    results.remove(results[0])



print(f'Team won {win} games.')
print(f'Team lost {lose} games.')
print(f'Drawn games: {draw}')


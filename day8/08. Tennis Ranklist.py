import math

WINNER_POINTS = 2000
FINALIST_POINTS = 1200
SEMI_FINALIST_POINTS = 720

number_of_championships = int(input())
starting_points_in_ranking = int(input())
total_points = 0
average_points_won_per_championship = 0
count_won_championships = 0
count_semi_finals = 0
count_finals = 0

for _ in range(number_of_championships):
    type_championship = input()

    if type_championship == 'W':
        starting_points_in_ranking += WINNER_POINTS
        count_won_championships += 1
    elif type_championship == 'SF':
        starting_points_in_ranking += SEMI_FINALIST_POINTS
        count_semi_finals += 1
    elif type_championship == 'F':
        starting_points_in_ranking += FINALIST_POINTS
        count_finals += 1

points_for_winning = count_won_championships * WINNER_POINTS
points_for_finals = count_finals * FINALIST_POINTS
points_for_semi_finals = count_semi_finals * SEMI_FINALIST_POINTS
average_points_won_per_championship = (points_for_winning
                                       + points_for_semi_finals
                                       + points_for_finals) / number_of_championships
total_points = starting_points_in_ranking

percentage_won_championships = (count_won_championships / number_of_championships) * 100

print(f'Final points: {total_points}')
print(f'Average points: {math.floor(average_points_won_per_championship)}')
print(f'{percentage_won_championships:.2f}%')

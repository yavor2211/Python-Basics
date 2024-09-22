THRESHOLD_MUSALA_HIKERS = 5
THRESHOLD_MONBLANC_HIKERS = 12
THRESHOLD_KILIMANDJARO = 25
THRESHOLD_K2 = 40

count_musala = 0
count_monblanc = 0
count_kilimandjaro = 0
count_k2 = 0
count_everest = 0

groups_of_hikers = int(input())
total_people = 0

for _ in range(groups_of_hikers):

    number_of_people = int(input())

    if number_of_people <= THRESHOLD_MUSALA_HIKERS:
        count_musala += number_of_people
    elif THRESHOLD_MUSALA_HIKERS < number_of_people <= THRESHOLD_MONBLANC_HIKERS:
        count_monblanc += number_of_people
    elif THRESHOLD_MONBLANC_HIKERS < number_of_people <= THRESHOLD_KILIMANDJARO:
        count_kilimandjaro += number_of_people
    elif THRESHOLD_KILIMANDJARO < number_of_people <= THRESHOLD_K2:
        count_k2 += number_of_people
    else:
        count_everest += number_of_people

total_people = count_musala + count_monblanc + count_kilimandjaro + count_k2 + count_everest



percentage_musala=(count_musala/total_people) * 100
percentage_montblanc=(count_monblanc/total_people) * 100
percentage_kilimandjaro=(count_kilimandjaro/total_people) * 100
percentage_k2=(count_k2/total_people) * 100
percentage_everest=(count_everest/total_people) * 100

print(f'{percentage_musala:.2f}%')
print(f'{percentage_montblanc:.2f}%')
print(f'{percentage_kilimandjaro:.2f}%')
print(f'{percentage_k2:.2f}%')
print(f'{percentage_everest:.2f}%')


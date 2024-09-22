input_text = input()
# буква	a	e	i	o	u
# стойност	1	2	3	4	5
direct_sum = 0

for i in input_text:
    if i == 'a':
        direct_sum += 1
    elif i == 'e':
        direct_sum += 2
    elif i == 'i':
        direct_sum += 3
    elif i == 'o':
        direct_sum += 4
    elif i == 'u':
        direct_sum += 5

print(direct_sum)

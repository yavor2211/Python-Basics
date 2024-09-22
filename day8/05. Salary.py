FINE_FOR_FACEBOOK=150
FINE_FOR_INSTAGRAM=100
FINE_FOR_REDDIT=50

open_tabs=int(input())
salary=int(input())
result = ''
for _ in range(open_tabs):
    website=input()

    if website == 'Facebook':
        salary-=FINE_FOR_FACEBOOK
    elif website == 'Instagram':
        salary-=FINE_FOR_INSTAGRAM
    elif website == 'Reddit':
        salary-=FINE_FOR_REDDIT

    if salary <=0:
        result=f'You have lost your salary.'
        break
else:
    result = salary

print(result)

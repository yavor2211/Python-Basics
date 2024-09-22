NUMBER_ONE=int(input())
NUMBER_TWO=int(input())
OPERATOR=input()

print_text=''

if OPERATOR == '+':
    print_text=(f'{NUMBER_ONE} + {NUMBER_TWO} = {NUMBER_ONE+NUMBER_TWO} {"- even"  if (NUMBER_ONE+NUMBER_TWO) % 2 ==0 else "- odd"}')
elif OPERATOR == '-':
    print_text = (f'{NUMBER_ONE} - {NUMBER_TWO} = {NUMBER_ONE - NUMBER_TWO} {"- even" if (NUMBER_ONE - NUMBER_TWO) % 2 == 0 else "- odd"}')
elif OPERATOR == '*':
    print_text = (f'{NUMBER_ONE} * {NUMBER_TWO} = {NUMBER_ONE * NUMBER_TWO} {"- even" if (NUMBER_ONE * NUMBER_TWO) % 2 == 0 else "- odd"}')
elif NUMBER_TWO == 0:
    print_text= (f'Cannot divide {NUMBER_ONE} by zero')
elif OPERATOR == '/':
    print_text = (f'{NUMBER_ONE} / {NUMBER_TWO} = {NUMBER_ONE / NUMBER_TWO:.2f}')
else:
    print_text = (f'{NUMBER_ONE} % {NUMBER_TWO} = {NUMBER_ONE % NUMBER_TWO}')

print(print_text)
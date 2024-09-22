deposit=float(input())
time_of_deposit=int(input())
percentage=float(input())
interest=deposit*percentage
interest_for_one_month=interest/12





sum=deposit+time_of_deposit*((deposit*interest)/12)
print(sum)
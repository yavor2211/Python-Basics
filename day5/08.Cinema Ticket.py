# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя
# и принтира на конзолата цената на билет за кино според деня от седмицата:
# Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
# 12	      12	14	            14	       12	    16        16
day_of_the_week=input()
price = 0
if day_of_the_week == 'Monday':
    price = 12
elif day_of_the_week == 'Tuesday':
    price = 12
elif day_of_the_week == 'Wednesday':
    price = 14
elif day_of_the_week == 'Thursday':
    price = 14
elif day_of_the_week == 'Friday':
    price = 12
elif day_of_the_week == 'Saturday':
    price = 16
elif day_of_the_week == 'Sunday':
    price = 16

print(price)
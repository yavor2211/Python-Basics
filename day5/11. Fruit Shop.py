# Магазин за плодове през работните дни работи на следните цени:
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.50	1.20	  0.85	   1.45	    2.70	   5.50	    3.85
# През събота и неделя магазинът работи на по-високи цени:l# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.70	1.25	0.90	1.60	    3.00	  5.60	    4.20

fruit = input()
day_of_the_week = input()
quantity = float(input())
price = 0
if (day_of_the_week == 'Monday'
        or day_of_the_week == 'Tuesday'
        or day_of_the_week == 'Wednesday'
        or day_of_the_week == 'Thursday'
        or day_of_the_week == 'Friday'):
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
elif day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20

if price != 0:
    total_price = price * quantity
    print(f'{total_price:.2f}')
else:
    print('error')

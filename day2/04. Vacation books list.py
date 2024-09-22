
pages_at_the_moment= int(input())

pages_for_one_hour=int(input())

days_for_reading=int(input())
hours_reading=pages_at_the_moment//pages_for_one_hour
hours_per_day=hours_reading/days_for_reading
#Изход
#Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
print(hours_per_day)
# Петя има магазин за детски играчки.
# Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
rent_price=0.10
puzzle_price=2.60
doll_price=3.00
bear_price=4.10
minion_price=8.20
truck_price=2.00
discount_price=0.25
price_trip=float(input())
puzzle=int(input())
doll=int(input())
bear=int(input())
minion=int(input())
truck=int(input())
sum=(puzzle*puzzle_price)+(doll*doll_price)+(bear*bear_price)+(minion*minion_price)+(truck*truck_price)
sum_toys=puzzle+doll+bear+minion+truck
discount=0
if sum_toys >=50:
    discount=sum*discount_price
else:
    discount=0


total_sum=sum-discount
rent=total_sum*rent_price
earnings=total_sum-rent
earnings_after_trip=earnings-price_trip
earnings_after_trip_2=price_trip-earnings
if earnings >= price_trip:
    print(f"Yes! {earnings_after_trip:0.2f} lv left.")
elif earnings <= price_trip:
    print(f"Not enough money! {earnings_after_trip_2:0.2f} lv needed.")

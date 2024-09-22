# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
# •	Пилешко меню –  10.35 лв.
chicken=10.35
# •	Меню с риба – 12.40 лв.
fish=12.40
# •	Вегетарианско меню  – 8.15 лв.
vegan=8.15
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).

# Цената на доставка е 2.50 лв и се начислява най-накрая.
delivery=2.50
# Вход
# От конзолата се четат 3 реда:
# •	Брой пилешки менюта – цяло число в интервала [0 … 99]
chicken_menus=int(input())
# •	Брой менюта с риба – цяло число в интервала [0 … 99]
fish_menu=int(input())
# •	Брой вегетариански менюта – цяло число в интервала [0 … 99]
vegan_menu=int(input())
chicken_menu_price=chicken*chicken_menus
fish_menu_price=fish*fish_menu
vegan_menu_price=vegan*vegan_menu
total_price_menus=chicken_menu_price+fish_menu_price+vegan_menu_price
desert=total_price_menus*0.20
total_price_all=total_price_menus+desert+delivery
# Изход
# Да се отпечата на конзолата един ред:  "{цена на поръчката}"
print(total_price_all)
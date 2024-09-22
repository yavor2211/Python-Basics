
# ako броя на видеокартите е по-голям от този на процесорите получава
# 15% отстъпка от крайната сметка. Важат следните цени:
# •	Видеокарта – 250 лв./бр.
DISCOUNT=0.15
VIDEOCARD_PRICE=250
PROCESSOR_PRICE=0.35
RAM_PRICE=0.10
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.

budget=float(input())
videocards_quantity=int(input())
processors_quantity=int(input())
ram_quantity=int(input())

processor_price=(videocards_quantity*VIDEOCARD_PRICE)*PROCESSOR_PRICE
ram_price=(videocards_quantity*VIDEOCARD_PRICE)*RAM_PRICE
total_sum=(videocards_quantity*VIDEOCARD_PRICE)\
          +(ram_price*ram_quantity)\
          +(processors_quantity*processor_price)
if videocards_quantity>processors_quantity:
    total_sum=total_sum-(total_sum*DISCOUNT)

if total_sum>budget:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")
else:
    print(f"You have {budget-total_sum:.2f} leva left!")
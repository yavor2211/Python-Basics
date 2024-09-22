# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
DECOR_PERCENTAGE=0.10
AMOUNT_NEEDED_EXTRAS=151
CLOTHING_DISCOUNT=0.10

budget=float(input())
extras=int(input())
price_clothing=float(input())

decor_price=budget*DECOR_PERCENTAGE
clothing_sum=extras*price_clothing


if extras>=AMOUNT_NEEDED_EXTRAS:
    clothing_sum-=(clothing_sum*CLOTHING_DISCOUNT)

total_sum=clothing_sum+decor_price

if total_sum>budget:
   print("Not enough money!")
   print(f"Wingard needs {total_sum-budget:0.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {budget-total_sum:0.2f} leva left.")
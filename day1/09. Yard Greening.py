sqm_price=7.61
discount=0.18
sqm=float(input())
greening=sqm*sqm_price
discount_after=discount*greening
total_sum=greening-discount_after

print(f'The final price is: {total_sum} lv.')
print(f'The discount is: {discount_after} lv.')
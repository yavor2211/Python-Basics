pens_price = float(5.80)

markers_price = float(7.20)

one_liter_chemichal_price = float(1.20)

numbers_of_pens = int(input())

numbers_of_markers = int(input())

chemichal_amount = int(input())

percentage_discount = int(input()) / 100

sum = (numbers_of_pens * pens_price) + (numbers_of_markers * markers_price) + (
            one_liter_chemichal_price * chemichal_amount)

total_amount = sum - (sum * percentage_discount)

print(total_amount)

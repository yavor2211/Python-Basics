price_nylon=1.50
price_paint=14.50
price_thinner=5.00
additional_paint=0.10
additional_nylon=2
bags=0.40
price_per_hour=0.30



quantity_nylon=int(input())
quantity_paint=int(input())
quantity_thinner=int(input())
hours_needed=int(input())
quantity_nylon+=additional_nylon
quantity_paint+=(quantity_paint*additional_paint)
total_sum=(quantity_nylon*price_nylon) \
          + (quantity_paint*price_paint) \
          + (quantity_thinner*price_thinner) \
          + bags
price_for_workers=(total_sum*price_per_hour) * hours_needed

total_sum_2=total_sum+price_for_workers
print(total_sum_2)
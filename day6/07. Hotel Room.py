STUDIO_PRICE_MAY_OCTOBER = 50
APARTMENT_PRICE_MAY_OCTOBER = 65
STUDIO_PRICE_JUNE_SEPTEMBER = 75.20
APARTMENT_PRICE_JUNE_SEPTEMBER = 68.70
STUDIO_PRICE_JULY_AUGUST = 76
APARTMENT_PRICE_JULY_AUGUST = 77
STUDIO_DISCOUNT_MORE_THAN_7_MAY_OCT = 0.05
STUDIO_DISCOUNT_MORE_THAN_14_MAY_OCT = 0.30
STUDIO_DISCOUNT_MORE_THAN_14_JUNE_SEPT = 0.20
APARTMENT_DISCOUNT_MORE_THAN_14 = 0.10

month = input()
count_nights = int(input())
price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    price_studio += STUDIO_PRICE_MAY_OCTOBER * count_nights
    price_apartment += APARTMENT_PRICE_MAY_OCTOBER * count_nights

    if count_nights > 14:
        price_studio -= price_studio * STUDIO_DISCOUNT_MORE_THAN_14_MAY_OCT
        price_apartment -= price_apartment * APARTMENT_DISCOUNT_MORE_THAN_14

    elif count_nights > 7:
        price_studio -= price_studio * STUDIO_DISCOUNT_MORE_THAN_7_MAY_OCT

elif month == 'June' or month == 'September':
    price_studio += STUDIO_PRICE_JUNE_SEPTEMBER * count_nights
    price_apartment += APARTMENT_PRICE_JUNE_SEPTEMBER * count_nights

    if count_nights > 14:
        price_studio -= price_studio * STUDIO_DISCOUNT_MORE_THAN_14_JUNE_SEPT
        price_apartment -= price_apartment * APARTMENT_DISCOUNT_MORE_THAN_14

elif month == 'July' or month == 'August':
    price_studio += STUDIO_PRICE_JULY_AUGUST * count_nights
    price_apartment += APARTMENT_PRICE_JULY_AUGUST * count_nights

    if count_nights > 14:
        price_apartment -= price_apartment * APARTMENT_DISCOUNT_MORE_THAN_14

print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')

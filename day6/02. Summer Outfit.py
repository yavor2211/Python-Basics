DEGREES = int(input())
TIME_OF_DAY = input()
outfit = ''
shoes = ''
OUTFIT_MORNING_10_to_18 = 'Sweatshirt'
SHOES_MORNING_10_to_18 = 'Sneakers'
OUTFIT_AFTERNOON_10_to_18 = 'Shirt'
SHOES_AFTERNOON_10_to_18 = 'Moccasins'
OUTFIT_EVENING_10_to_18 = 'Shirt'
SHOES_EVENING_10_to_18 = 'Moccasins'
if 10 <= DEGREES <= 18:
    if TIME_OF_DAY == 'Morning':
        outfit = OUTFIT_MORNING_10_to_18
        shoes = SHOES_MORNING_10_to_18
    elif TIME_OF_DAY == 'Afternoon':
        outfit = OUTFIT_AFTERNOON_10_to_18
        shoes = SHOES_AFTERNOON_10_to_18
    elif TIME_OF_DAY == 'Evening':
        outfit = OUTFIT_EVENING_10_to_18
        shoes = SHOES_EVENING_10_to_18

OUTFIT_MORNING_18_to_24 = 'Shirt'
SHOES_MORNING_18_TO_24 = 'Moccasins'
OUTFIT_AFTERNOON_18_TO_24 = 'T-Shirt'
SHOES_AFTERNOON_18_TO_24 = 'Sandals'
OUTFIT_EVENING_18_TO_24 = 'Shirt'
SHOES_EVENING_18_TO_24 = 'Moccasins'
if 18 < DEGREES <= 24:
    if TIME_OF_DAY == 'Morning':
        outfit = OUTFIT_MORNING_18_to_24
        shoes = SHOES_MORNING_18_TO_24
    elif TIME_OF_DAY == 'Afternoon':
        outfit = OUTFIT_AFTERNOON_18_TO_24
        shoes = SHOES_AFTERNOON_18_TO_24
    elif TIME_OF_DAY == 'Evening':
        outfit = OUTFIT_EVENING_18_TO_24
        shoes = SHOES_EVENING_18_TO_24
OUTFIT_MORNING_25 = 'T-Shirt'
SHOES_MORNING_25 = 'Sandals'
OUTFIT_AFTERNOON_25 = 'Swim Suit'
SHOES_AFTERNOON_25 = 'Barefoot'
OUTFIT_EVENING_25 = 'Shirt'
SHOES_EVENING_25 = 'Moccasins'
if DEGREES >= 25:
    if TIME_OF_DAY == 'Morning':
        outfit = OUTFIT_MORNING_25
        shoes = SHOES_MORNING_25
    elif TIME_OF_DAY == 'Afternoon':
        outfit = OUTFIT_AFTERNOON_25
        shoes = SHOES_AFTERNOON_25
    elif TIME_OF_DAY == 'Evening':
        outfit = OUTFIT_EVENING_25
        shoes = SHOES_EVENING_25

print(f"It's {DEGREES} degrees, get your {outfit} and {shoes}.")

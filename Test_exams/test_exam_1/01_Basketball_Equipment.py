tax_for_playing_a_year=int(input())
basketball_sneakers=tax_for_playing_a_year-(tax_for_playing_a_year*0.40)
basketball_jerseys=basketball_sneakers-(basketball_sneakers*0.20)
basketball=basketball_jerseys/4
basketball_accessories=basketball/5

total_price=tax_for_playing_a_year\
            +basketball_sneakers\
            +basketball_jerseys\
            +basketball\
            +basketball_accessories

print(f'{total_price:.2f}')

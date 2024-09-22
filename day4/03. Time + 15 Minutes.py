# Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя
MINUTES_IN_HOUR=60
HOURS_IN_DAY=24
TIME_AFTER=15
# и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути.
# Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
hours=int(input())
minutes=int(input())
# Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две цифри,
# с водеща нула, когато е необходимо
minutes+=TIME_AFTER

if minutes>=MINUTES_IN_HOUR:
    minutes-=MINUTES_IN_HOUR
    hours+=1
if hours>=HOURS_IN_DAY:
    hours-=HOURS_IN_DAY

print(f'{hours}:{minutes:02d}')
days = int(input())

years = int(days / 360)
print(f"{years} ano(s)")

days_remainning1 = days - (years * 365)

months = int(days_remainning1 / 30)
print(f"{months} mes(es)")

days_remainning2 = days_remainning1 - (months * 30)
print(f"{days_remainning2} dia(s)")

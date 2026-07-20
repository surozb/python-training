from datetime import date


print('Gamer, Daicha')
today = date.today()
print('Today date is:', today)
target_date = date(2026, 9, 13)
remaining_days = (target_date - today).days
print('Remaining days until September 13, 2026:', remaining_days)
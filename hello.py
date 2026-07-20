from datetime import date


print('Gamer, Daicha')
today = date.today()
print(f'Today date is: {today}')
target_date = date(2026, 9, 13)
remaining_days = (target_date - today).days
print(f'Remaining days until {target_date:%B %d, %Y}: {remaining_days}')
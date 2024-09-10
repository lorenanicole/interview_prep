import calendar
import datetime

dates = []
initial_date = datetime.datetime(2024, 1, 31)
num_transfers = 4

for indx in range(num_transfers - 1):
    # print(f'Here I am! {initial_date} {indx}')
    if len(dates) == 0:
        date = initial_date
    else:
        date = dates[-1]

    if date.month == 12:
        days_in_month = calendar.monthrange(date.year + 1, 1)
        print(f'Days in month: {days_in_month} inside if')
        date = date.replace(month=1, day=days_in_month[1])
        print(date)
    else:
        days_in_month = calendar.monthrange(date.year, date.month + 1)
        print(f'Days in month: {days_in_month} inside else')
        date = date.replace(month=date.month +1, day=days_in_month[1])
    print(date)
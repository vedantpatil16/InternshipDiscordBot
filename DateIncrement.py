import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

# Get the current datetime
current_datetime = datetime.datetime(2023, 12, 15, 0, 0, 0)
print(current_datetime)
# Increment the month by one
new_datetime = current_datetime + relativedelta(minutes=5)
print(new_datetime)

current = datetime.datetime.now()
extra =  current + relativedelta(months=2)

print(extra.month)

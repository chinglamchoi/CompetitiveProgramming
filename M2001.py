from datetime import date
from datetime import timedelta
# I know, I'm lazy

months = {"JAN":1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8, "SEP":9, "OCT":10, "NOV":11, "DEC":12}
months1 = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

a,b = input().split(" ")
b = int(b)
a1 = months[a]
inn = date(year=2020, month=a1, day=b)
outt = inn + timedelta(days=14)
print(months1[outt.month-1], outt.day)

from datetime import date
import datetime
a = input()
dt = a + "-2-14"
year, month, day = (int(x) for x in dt.split('-'))
b = datetime.date(year, month, day).weekday()
if b == 0:
    print("Monday")
elif b == 1:
    print("Tuesday")
elif b == 2:
    print("Wednesday")
elif b == 3:
    print("Thursday")
elif b == 4:
    print("Friday")
elif b == 5:
    print("Saturday")
else:
    print("Sunday")

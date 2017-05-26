#get the users date of birth
#month of birth
#current year
import calendar
#print exact day of the week the user was born
age = int (input("Enter your age:"))
date= int (input("Enter your date of birth:"))
month= int (input("Enter your month of birth(1-12):"))
currentyear=int(input("Enter your current year:"))

year=currentyear-age
weekday=calendar.weekday(year,month,date)
dayofweek=calendar.day_name[weekday]
monthstring=calendar.month_name[month]

print("You were born on a "+ str(date)+ " " + monthstring + " " +str(year) + " on a " + dayofweek)


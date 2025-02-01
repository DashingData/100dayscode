# to check if the given year is a leap year or not

year = int(input("Enter the year:"))
if (year % 400 == 0) and (year % 100 == 0):
    print("The year  leap year")
elif (year % 4 == 0 ) and (year % 100 != 0):
    print("The year is a leap year")
else:
    print("the year is not a leap year")
    
          


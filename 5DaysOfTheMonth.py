mo_days = {
    1: 31, #JANUARY MONTH,
    2: 28, #FEBRUARY MONTH,
    3: 31, #MARCH MONTH,
    4: 30, #APRIL MONTH,
    5: 31, #MAY MONTH,
    6: 30, #JUNE MONTH,
    7: 31, #JULY MONTH,
    8: 31, #AUGUST MONTH,
    9: 30, #SEPTEMBER MONTH,
    10: 31, #OCTOBER MONTH,
    11: 30, #NOVEMBER MONTH,
    12: 31, #DECEMBER MONTH
}
    
#This is where I will properly put the month names according to days
mo_names = {
    1: "JANUARY", 
    2: "FEBRUARY", 
    3: "MARCH", 
    4: "APRIL", 
    5: "MAY", 
    6: "JUNE", 
    7: "JULY", 
    8: "AUGUST", 
    9: "SEPTEMBER", 
    10: "OCTOBER", 
    11: "NOVEMBER", 
    12: "DECEMBER"
}
    
print("Below is the Days in Month Calculator")
print("Please enter a month number (1-12) if you wish to know such information" )

month = int(input("Month: "))
#To only check if the user's input is valid
if month in mo_days:
    days = mo_days[month]
    mo_names = mo_names[month]
    print(f"\n{mo_names} has {days} days.")
        
    #Since February has leap year, the program would have to include this additional program
    if month == 2:
        print("FYI, FEBRUARY has 29 days in leap years.")
else:
    print("That is an invalid number. Only enter any number that's between 1-12")
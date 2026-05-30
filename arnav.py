entry = int(input("Enter morning time  = "))
exit = int(input("Enter evening time  = "))

if entry <= 8 and exit == 18:
        print("full day")
elif entry <= 8 and exit >= 18:
        print("Overtime")
elif 7 <= entry <= 8 and 13 <= exit <= 17 :
        print("Morning Half Day")
elif 9 <= entry <= 13 and exit >= 18:
        print("Evening Half Day")
elif entry <= 8 and exit <= 12 or entry >= 13 and exit <= 18:
        print("Short Day")
else:
        print("Invalid time")
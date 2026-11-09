#Write a program that allows you to convert time in 24-hour format to 12-hour format. The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

#Enter time (24-hour format): 16:32
#Time in 12-hour format: 4:32pm

time_change = "0"
Enter_Time = input("Enter time in 24 hour format: (hh:mm) ")
#print(Enter_Time[0:2])
if Enter_Time[0:2] == "13":
    time_change = "1"
elif Enter_Time[0:2] == "14":
    time_change = "2"
elif Enter_Time[0:2] == "15":
    time_change = "3"
elif Enter_Time[0:2] == "16":
    time_change = "4"
elif Enter_Time[0:2] == "17":
    time_change = "5"
elif Enter_Time[0:2] == "18":
    time_change = "6"
elif Enter_Time[0:2] == "19":
    time_change = "7"
elif Enter_Time[0:2] == "20":
    time_change = "8"
elif Enter_Time[0:2] == "21":
    time_change = "9"
elif Enter_Time[0:2] == "22":
    time_change = "10"
elif Enter_Time[0:2] == "23":
    time_change = "11"
elif Enter_Time[0:2] == "24":
    time_change = "12"    
else:
    time_change = Enter_Time
am_or_pm = 0 
if len(Enter_Time) >= 12 and len(Enter_Time) <= 0:
    am_or_pm = "am"
else:
    am_or_pm = "pm"
zam_or_pm = 0
if len(time_change) >= 12 and len(time_change) <= 0:
    zam_or_pm = "am"
else:
    zam_or_pm = "pm"


    
print(f'Time before 12h change {Enter_Time}{am_or_pm} and after {time_change}{Enter_Time[2:5]} {zam_or_pm} ')


#Write a program that allows you to convert time in 24-hour format to 12-hour format. The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

#Enter time (24-hour format): 16:32
#Time in 12-hour format: 4:32pm

Enter_Time = input("Enter time in 24 hour format: (hh:mm) ")
Time_in_12h_format = ""
if Enter_Time[0] == '1' or Enter_Time[0] == '2' or Enter_Time[0] == '3' or Enter_Time[0] == '4' or Enter_Time[0] == '5' or Enter_Time[0] == '6' or Enter_Time[0] == '7' or Enter_Time[0] == '8' or Enter_Time[0] == '9' or Enter_Time[0:1] == '10'or Enter_Time[0:1] == '11' or Enter_Time[0:1] == '12':    
    Time_in_12h_format == Enter_Time
elif Enter_Time[0:1] == "13":
    Time_in_12h_format[0:1] = "1" 




print(f"time before change {Enter_Time} and after {Time_in_12h_format}")
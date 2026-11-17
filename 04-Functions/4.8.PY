
#def time_string(hours, minutes, time_format): 
  #  hours = int(input('Enter hours'))
   # minutes = input('Enter minutes')
   # time_format = int(input('Enter Time format 12h or 24h :'))
   # if time_format == 24:
   #     hours = hours 
  #      minutes = minutes 
  #  elif time_format == 12:
 #       if hours > 12 and hours < 24:
  #          hours = hours - time_format
   #         minutes == minutes
            
   #     else: 
    #        hours == hours
   #         return hours
  #      return hours
  #  return time_format


def time_string(hours, minutes, time_format):
    if time_format == 24:
        return f"{hours:02d}:{minutes:02d}"

    elif time_format == 12:
        if 12 < hours < 24:
            hours = hours - 12
        elif hours == 0:
            hours = 12
        return f"{hours}:{minutes:02d}"


print(f"time for 14:22 in 12h format: {time_string(14, 22, 12)}")
print(f"time for 14:22 in 24h format: {time_string(14, 22, 24)}")



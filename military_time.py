# Military Time
from IPython.display import clear_output
import re

def mil_time():
    t = True
    regex = r"^(1[012]|[1-9]):[0-5][0-9]\s(AM|PM)$"
    while t:
        time = input("Enter a time to convert (e.g. 2:30 PM or 12:45 AM): ")
        
        if re.match(regex, time):
            t = False
        
        else:    
            clear_output()
            print(f"You did not type the time correctly. You typed: {time}")
            t = True
    
    clear_output()
    print(f'Time: {time}')
    
    if time[0:2] == '12' and 'AM' in time:
        time = f'00:{time[3:5]}'
    
    elif time[0:2] == '11' and 'AM' in time:
        time = time[:5]

    elif time[0:2] == '12' and 'PM' in time:
        time = time[:5]
    
    elif 'PM' in time and len(time) == 8 :
        time = str(12 + int(time[0:2])) + time[2:5]
    
    elif 'PM' in time and len(time) == 7:
        time = str(12 + int(time[0])) + time[1:4]
    
    else:
        time = f'0{time[:4]}'
        
    print(f'Military Time: {time}')

if __name__ == "__main__":
    mil_time()
import datetime
import time
import threading

alarms = [] #Stores all set alarms

class Alarm:
    def __init__(self, hour, minute, name):
        self.hour = hour
        self.minute = minute
        self.name = name

def set_alarm():
    #Various flags that track where the user is in creating the alarm
    get_input = True
    get_hour = True
    get_minute = False
    progress = False
    set_alarm = False
    
    print("\nPlease use the 24 hour time format")
    
    while get_input == True: #Loops the function until the user cancels or creates an alarm
        if get_hour == True:
            print("\nEnter the hour you want to set for the alarm. Enter \"Cancel\" to exit")
            hour = str(input())

            if hour.lower() == "cancel": #Checks if the user wants to cancel
                get_input = False
            else:
                progress = True #Allows the function to verify the input

            if progress == True:
                invalid = False
                progress = False
                
                for i in hour: #Checks for invalid characters in the input
                    if i.isalpha():
                        invalid = True
                        
                if invalid == True:
                    print("\nPlease enter the hour using numbers")
                        
                else:
                        
                    if len(hour) == 2: #Checks the length of the input to verify it
                        if int(hour) >= 0 and int(hour) < 24:
                            get_minute = True
                            get_hour = False
                            hour = int(hour)

                        else:
                            print("\nPlease use the 24 hour time format")
                            
                    else:
                        print("\nPlease enter two numbers")

        if get_minute == True:
            print("\nEnter the minute you want to set for the alarm. Enter \"Back\" to re-enter the hour or enter \"Cancel\" to cancel.")
            minute = str(input())

            if minute.lower() == "cancel":
                get_input = False

            elif minute.lower() == "back":
                hour = ""
                get_minute = False
                get_hour = True

            else:
                progress = True

            if progress == True:
                invalid = False
                progress = False

                for i in minute:
                    if i.isalpha():
                        invalid = True

                if invalid == True:
                    print("\nPlease enter the minute using numbers")

                else:

                    if len(minute) == 2:
                        if int(minute) >= 0 and int(minute) < 60:
                            get_input = False
                            get_minute = False
                            set_alarm = True
                            minute = int(minute)
                            print("\nEnter the name for this alarm")
                            name = str(input())

                        else:
                            print("\nPlease enter a valid minute")

                    else:
                        print("\nPlease enter two numbers")

    if set_alarm == True: #Sets the alarm
        temp = datetime.time(hour,minute)
        alarm = Alarm(temp.hour,temp.minute,name)
        return alarm

def check_alarm():
    while len(alarms) > 0:
        temp_time = time.ctime() #Gets the current time
        
        c_hour = temp_time[11] + temp_time[12] #Seperates the relavent data from the current time
        c_minute = temp_time[14] + temp_time[15]

        c_time = datetime.time(int(c_hour),int(c_minute)) #Converts the current time into the same format used for the alarms

        repeat = True
        
        while repeat == True: #Loop is used to catch any alarms that might get skipped over when removing items from the list
            repeat = False
            for i in alarms: #Uses the alarms global variable
                if i.hour == c_time.hour and i.minute == c_time.minute:
                    print(i.name, "alarm")
                    alarms.remove(i)
                    repeat = True

        print("Woo")
        time.sleep(10) #loops the function every 10 seconds



alarms.append(set_alarm()) #Gets user input for an alarm


threading.Thread(target = check_alarm).start() #Starts the thread that checks all alarms

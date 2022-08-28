#This function greets the user based on the time of the day
import datetime


class DaytimeGreeter:
    

    
    
    def give_greeting():
        currentTime = datetime.datetime.now()
        ct = currentTime.hour

        if ct < 12:
            greeting = "Good morning"
        elif 12 <= currentTime.hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        
        return greeting

    def greeted_name():
        name = input("Enter your name:")
        print(DaytimeGreeter.give_greeting, name)
        
    greeted_name()
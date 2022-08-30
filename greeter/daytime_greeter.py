#This function greets the user based on the time of the day
import datetime


class DaytimeGreeter:

    def give_greeting(name):
        if not name:
            return "Please enter your name"

        currentTime = datetime.datetime.now()
        ct = currentTime.hour

        if ct < 12:
            greeting = "Good morning"
        elif 12 <= ct < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        
        return greeting + " " + name

   
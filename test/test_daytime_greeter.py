import pytest
import datetime

from greeter.daytime_greeter import DaytimeGreeter

# This class contains tests for daytime_greeter module

class TestGreeter:

    def test_greeter_with_valid_name(self):
        name = "Ameya"
        currentTime = datetime.datetime.now()
        greeting =""
        if currentTime.hour < 12:
            greeting = "Good morning"
        elif 12 <= currentTime.hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        assert DaytimeGreeter.give_greeting(name) == greeting+" "+name

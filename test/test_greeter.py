import pytest
import datetime

from greeter.greeter import Greeter

# This class contains tests for greeter module

class TestGreeter:

    def test_greeter_with_valid_name(self):
        name = "Tom"
        assert Greeter.greet(name) == "Hello Tom. Have a great day!"

    def test_greeter_with_no_name(self):
        assert Greeter.greet("") == "Please provide a name."
"""
Academic Activity: Fan Representation Implementation
Enforcing strict Object-Oriented Programming and Encapsulation principles.
"""

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", is_on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__is_on = is_on
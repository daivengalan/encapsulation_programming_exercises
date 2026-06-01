class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", is_on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__is_on = is_on

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_is_on(self):
        return self.__is_on
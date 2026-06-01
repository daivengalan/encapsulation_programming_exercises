class Fan:
    SLOW = 1; MEDIUM = 2; FAST = 3
    def __init__(self, speed=SLOW, radius=5.0, color="blue", is_on=False):
        self.__speed = speed; self.__radius = radius; self.__color = color; self.__is_on = is_on
    def get_speed(self): return self.__speed
    def get_radius(self): return self.__radius
    def get_color(self): return self.__color
    def get_is_on(self): return self.__is_on
    def set_speed(self, speed):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]: self.__speed = speed
    def set_radius(self, radius):
        if radius > 0: self.__radius = radius
    def set_color(self, color):
        if isinstance(color, str) and color.strip(): self.__color = color
    def set_is_on(self, is_on):
        if isinstance(is_on, bool): self.__is_on = is_on

def run_test_fan_program():
    print("=== RUNNING FAN UTILITY SIMULATION ===")
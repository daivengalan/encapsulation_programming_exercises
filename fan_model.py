class Fan:
    SLOW = 1;
    MEDIUM = 2;
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", is_on=False):
        self.__speed = speed;
        self.__radius = radius;
        self.__color = color;
        self.__is_on = is_on

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_is_on(self):
        return self.__is_on

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

    primary_fan = Fan()
    primary_fan.set_speed(Fan.FAST)
    primary_fan.set_radius(10.0)
    primary_fan.set_color("yellow")
    primary_fan.set_is_on(True)

    secondary_fan = Fan()
    secondary_fan.set_speed(Fan.MEDIUM)
    secondary_fan.set_radius(5.0)
    secondary_fan.set_color("blue")
    secondary_fan.set_is_on(False)

    print("\n[Primary Fan Unit Status]")
    print(f"Operational Speed : {primary_fan.get_speed()}")
    print(f"Physical Radius   : {primary_fan.get_radius()} units")
    print(f"Chassis Color     : {primary_fan.get_color()}")
    print(f"Power State Active: {primary_fan.get_is_on()}")

    print("\n[Secondary Fan Unit Status]")
    print(f"Operational Speed : {secondary_fan.get_speed()}")
    print(f"Physical Radius   : {secondary_fan.get_radius()} units")
    print(f"Chassis Color     : {secondary_fan.get_color()}")
    print(f"Power State Active: {secondary_fan.get_is_on()}")


if __name__ == "__main__":
    run_test_fan_program()
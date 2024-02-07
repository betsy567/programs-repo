class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    # Getter methods to access private attributes
    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    # Overloading the + operator
    def __add__(self, other_time):
        total_seconds = (self.__hour + other_time.get_hour()) * 3600 + \
                        (self.__minute + other_time.get_minute()) * 60 + \
                        (self.__second + other_time.get_second())

        # Calculate new hours, minutes, and seconds
        new_hour, remainder = divmod(total_seconds, 3600)
        new_minute, new_second = divmod(remainder, 60)

        # Create a new Time object with the result
        result_time = Time(new_hour, new_minute, new_second)
        return result_time

# Example usage
time1 = Time(2, 30, 45)
time2 = Time(1, 15, 20)

sum_time = time1 + time2

print("Time 1:", time1.get_hour(), "hours", time1.get_minute(), "minutes", time1.get_second(), "seconds")
print("Time 2:", time2.get_hour(), "hours", time2.get_minute(), "minutes", time2.get_second(), "seconds")
print("Sum:", sum_time.get_hour(), "hours", sum_time.get_minute(), "minutes", sum_time.get_second(), "seconds")

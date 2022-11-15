def type_check(input_given, type_wanted) -> bool:
    if type(input_given) == type_wanted:
        return True


def range_check(input_given: int | float, min_value: int | float, max_value: int | float) -> bool:
    if min_value < input_given < max_value:
        return True


def length_check(input_given, len_value: int) -> bool:
    if len(input_given) == len_value:
        return True


# Checks for valid date when given in ISO 6801 format YYYY-MM-DD
def valid_date(input_given: str) -> bool:
    def is_leap(year: int) -> bool:
        # A year is leap if it is divisible by 4
        # But if the year is a century year it has to be divisible by 400
        if year % 400 == 0:
            return True
        elif year % 100 == 0 and year % 4 == 0:
            return True

    def valid_day_and_month(day: int, month: int, leap: bool) -> bool:
        match month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                if 0 < day <= 31:
                    return True
            case 4 | 6 | 9 | 11:
                if 0 < day <= 30:
                    return True
            case 2:
                if leap and 0 < day <= 29:
                    return True
                elif 0 < day <= 28:
                    return True
            case _:
                return False

    def correct_format(date: str) -> bool:
        if len(date) == 10 and (date[4] + date[7]) == "--":
            return True

    def separate_values(date: str) -> tuple:
        try:
            year = int(date[0:3])
            month = int(date[5:7])
            day = int(date[8:10])
        except ValueError:
            return False
        return year, month, day

    if correct_format(input_given):
        year, month, day = separate_values(input_given)
        if valid_day_and_month(day, month, is_leap(year)):
            return True


# Checks time in the ISO 8601 format hh:mm:ss
def valid_time(input_given: str) -> bool:
    def correct_format(time: str):
        if len(time) == 8 and (time[2] + time[5]) == "::":
            return True

    def seperate_values(time: str) -> tuple:
        try:
            hour = int(time[0:2])
            minute = int(time[3:5])
            second = int(time[6:8])
        except ValueError:
            return False
        return hour, minute, second

    if correct_format(input_given):
        hour, minute, second = seperate_values(input_given)
        if (0 <= hour < 24) and (0 <= minute < 60) and (0 <= second < 60):
            return True

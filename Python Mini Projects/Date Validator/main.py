def is_leap(year: int) -> bool:
    # A year is leap if it is divisible by 4
    # But if the year is a century year it has to be divisible by 400
    if year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
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
        month = int(date[5] + date[6])
        day = int(date[8] + date[9])
    except ValueError:
        return
    return year, month, day


def valid_date(date) -> bool:
    if correct_format(date):
        year, month, day = separate_values(date)
        if valid_day_and_month(day, month, is_leap(year)):
            return True


def main():
    while True:
        date = input("Please enter a date (YYYY-MM-DD):\n > ")
        if valid_date(date):
            print("That's a valid date!")
            break
        print("Oops! That's an invalid date, please try again!")


if __name__ == "__main__":
    main()

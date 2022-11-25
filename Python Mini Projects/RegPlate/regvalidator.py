def get_details() -> tuple:
    year = 0
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    has_reg = input("Do you have a registration number? (y/n): ").lower()
    if has_reg in ["y", "yes"]:
        year = input("Enter the year of your registration: ")
        try:
            year = int(year)
        except ValueError:
            print("Invalid year")
            get_details()
    return name, phone, has_reg, year


def get_reg() -> str:
    reg = input("Enter your registration number: ")
    return reg


def validate_reg(reg: str) -> bool:
    reg = reg.upper().replace("I", "").replace("Q", "").replace("Z", "")
    if len(reg) == 8:
        if reg[0:2].isalpha() and reg[2:4].isdigit() and reg[4] == " " and reg[5:8].isalpha():
            return True
    return False

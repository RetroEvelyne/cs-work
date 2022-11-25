import regvalidator
import findreg
import jsonutils
import sys


def get_data() -> dict:
    name, phone, has_reg, year = regvalidator.get_details()
    data = {"name": name, "phone": phone, "reg": regvalidator.get_reg(), "year": year}
    return data


def registration():
    data = get_data()
    try:
        year = int(data["year"])
    except ValueError:
        print("Invalid year")
        get_data()
    if year < 2001:
        jsonutils.write_json_file("regdata.json", data)
        print("Registration number saved")
    else:
        if regvalidator.validate_reg(data["reg"]):
            jsonutils.write_json_file("regdata.json", data)
            print("Registration number saved")


def find_reg():
    reg = regvalidator.get_reg()
    if regvalidator.validate_reg(reg):
        name, phone = findreg.find_reg_from_json(reg)
        print(f"Name: {name}\n"
              f"Phone: {phone}\n"
              f"Registration: {reg}")
        input("Press enter to continue")
        menu()
    else:
        print("Invalid Registration Number")
        input("Press enter to continue")
        menu()


def menu():
    print("1. Enter Registration Plate")
    print("2. Find Registration Plate")
    print("3. Exit")
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid Choice")
        menu()
    match choice:
        case 1:
            registration()
        case 2:
            find_reg()
        case 3:
            sys.exit()
        case _:
            print("Invalid Choice")
            menu()


if __name__ == "__main__":
    menu()

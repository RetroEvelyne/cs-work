import colors
import json
from random import choice


def get_colors(bands_json):
    colours = []
    errors = [f"{colors.red}Hey That's Not Valid!\n{colors.norm}",
              f"{colors.red}Oi! Stop It!\n{colors.norm}",
              f"{colors.red}Stop It Now!\n{colors.norm}",
              f"{colors.red}No! Go Back! I Want To Be Monkey!\n{colors.norm}",
              f"{colors.red}Your Brain Failed Successfully\n{colors.norm}"]
    number_things = ["1st", "2nd", "3rd", "4th", "5th"]

    for i in range(5):
        valid = False
        while not valid:
            band = input(f"What Is Your {number_things[i]} band\n ╰-> ").lower()
            if band in bands_json:
                if band == "none" and i == 4:
                    print(f"{colors.green}Thank You\n{colors.norm}")
                    valid = True
                    colours.append(band)
                elif band != "none":
                    if i < 3:
                        if "digit" in bands_json[band]:
                            print(f"{colors.green}Thank You\n{colors.norm}")
                            valid = True
                            colours.append(band)
                        else:
                            print(choice(errors))
                    else:
                        print(f"{colors.green}Thank You\n{colors.norm}")
                        valid = True
                        colours.append(band)
                else:
                    print(choice(errors))
            else:
                print(choice(errors))

    return colours


def calculate(bands_json, colours):
    final = ""

    # Add the first 3 bands as digits
    for i in range(3):
        final = final + str(bands_json[colours[i]]["digit"])

    # Do multiplication with 4th band
    final = str((int(final) * bands_json[colours[3]]["multi"]).__round__(2))

    # Add the tolerance on the end
    final = final + " ±" + str(bands_json[colours[4]]["tol"]) + "%"

    return final


def main():
    print(f"""{colors.purple}
    ***********************************************{colors.cyan}
        Hello Welcome To Resistor Calculator App{colors.purple}
    ***********************************************{colors.norm}
    """)

    with open("bands.json") as file:
        bands_json = json.load(file)

    colours = get_colors(bands_json)
    final = calculate(bands_json, colours)

    print(f"Your Resistor Is {final} Ω")


if __name__ == "__main__":
    main()

import ansi
import json


def get_colors(bands_json):
    colors = []
    number_things = ["1st", "2nd", "3rd", "4th", "5th"]

    for i in range(5):
        valid = False
        while not valid:
            band = input(f"What Is Your {number_things[i]} Band\n ╰-> ").lower()
            if band in bands_json:
                if band == "none" and i == 4:
                    print(f"{ansi.green}Thank You\n{ansi.norm}")
                    valid = True
                    colors.append(band)
                elif band != "none":
                    if i < 3:
                        if "multi" in bands_json[band]:
                            print(f"{ansi.green}Thank You\n{ansi.norm}")
                            valid = True
                            colors.append(band)
                        else:
                            print(f"{ansi.red}Hey That's Not Valid!\n{ansi.norm}")
                    else:
                        print(f"{ansi.green}Thank You\n{ansi.norm}")
                        valid = True
                        colors.append(band)
                else:
                    print(f"{ansi.red}Hey That's Not Valid!\n{ansi.norm}")
            else:
                print(f"{ansi.red}Hey That's Not Valid!\n{ansi.norm}")

    return colors


def calculate(bands_json, colors):
    final = ""

    # Add the first 3 bands as digits
    for i in range(3):
        final = final + str(bands_json[colors[i]]["digit"])

    # Do multiplication with 4th band
    final = str((int(final) * bands_json[colors[3]]["multi"]).__round__(2))

    # Add the tolerance on the end
    final = final + "Ω ±" + str(bands_json[colors[4]]["tol"]) + "%"

    return final


def main():
    print(f"""{ansi.purple}
    ***********************************************{ansi.cyan}
        Hello Welcome To Resistor Calculator App{ansi.purple}
    ***********************************************{ansi.norm}
    """)

    with open("bands.json") as file:
        bands_json = json.load(file)

    colors = get_colors(bands_json)
    final = calculate(bands_json, colors)

    print(f"Your Resistor Is {final}")


if __name__ == "__main__":
    main()

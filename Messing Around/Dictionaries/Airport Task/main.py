import jsonutils


def jsonprint(data: dict):
    for i in data:
        print(f"| {data[i]}: {i}")


def ask():
    yes_no = input(f"\nWould You Like To Add Another? (y/n) \n> ").lower()



def main():
    airports = jsonutils.openfile("airports.json")
    print("These Are The Airports We Have In Our Database:")
    jsonprint(airports)
    ask()
    jsonutils.writetofile("airports.json", airports)


if __name__ == "__main__":
    main()

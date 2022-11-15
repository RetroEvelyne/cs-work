import jsonutils
from random import choice


def get_random_pair(d: dict):
    print(d.items())
    key, value = choice([d.items()])
    return key, value


def ask_question(question_number: int, table: dict):
    symbol, element = get_random_pair(table)
    print(symbol, element)


def main():
    table = jsonutils.open_file("table.json")
    for question_number in range(1, 11):
        ask_question(question_number, table)


if __name__ == "__main__":
    main()

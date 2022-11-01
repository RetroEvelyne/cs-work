import colors as c
from random import choice, randint


def get_answer(question_type: str, num1: int, num2: int) -> str:
    match question_type:
        case "*":
            return str(num1 * num2)
        case "/":
            return str(round((num1 / num2), 1))
        case "+":
            return str(num1 + num2)
        case "-":
            return str(num1 - num2)


def question(question_type: str, correct: int) -> int:
    num1 = randint(1, 12)
    num2 = randint(1, 12)
    answer = get_answer(question_type, num1, num2)

    if answer[-2:] == ".0":
        answer = answer[:(len(answer) - 2)]

    while True:
        if question_type != "/":
            user_answer = input(f"{c.red}{num1} {c.yellow}{question_type} {c.red}{num2} \n{c.purple}╰-> ")
        else:
            user_answer = input(f"{c.red}{num1} {c.yellow}{question_type} {c.red}{num2} (1dp)\n{c.purple}╰-> ")

        if user_answer == "pass":
            break

        try:
            float(user_answer)
            if user_answer == str(answer):
                correct += 1
                break
            else:
                print(f"{c.red}That Answer's Wrong, The Correct Answer Was {answer}")
                break
        except ValueError:
            print(f"{c.red}Error Has To Be A Number... Try Again")

    return correct


def main():
    right = 0
    question_num = 5
    for i in range(question_num):
        right = question(choice(["*", "/", "+", "-"]), right)
    print(f"{c.cyan}You Finished With {c.green}{right}{c.cyan}/{c.red}{question_num}")


if __name__ == "__main__":
    main()

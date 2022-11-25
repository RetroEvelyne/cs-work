from random import choices


def validate_answer(answer: str, random_letters: list[str]) -> int:
    if len(answer) > 10:
        return 0
    count = 0
    for i in answer:
        if i in random_letters:
            random_letters.remove(i)
            answer = answer.replace(i, "")
            count += 1
    return count


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    random_letters = str(choices(alphabet, k=10))
    random_letters = random_letters.replace("'", "").replace("[", "").replace("]", "").replace(",", "").replace(" ", "")
    print(f"Your letters are: {random_letters}")
    answer = input("Enter your answer: ").lower()
    score = validate_answer(answer, random_letters)
    print(f"Score: {score}")


if __name__ == "__main__":
    main()








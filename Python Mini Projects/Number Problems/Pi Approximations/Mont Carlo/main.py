from random import uniform


def main(n: int) -> float:
    in_circle = 0

    for i in range(n):

        x_coord = uniform(0, 1)
        y_coord = uniform(0, 1)

        if (x_coord**2) + (y_coord**2) <= 1:
            in_circle += 1

    return 4 * (in_circle / n)


if __name__ == "__main__":
    print(main(9999999))

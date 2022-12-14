import time


def get_triplets(m, n):
    a = 2 * m * n
    b = m ** 2 - n ** 2
    c = m ** 2 + n ** 2
    return a, b, c


if __name__ == "__main__":
    n = 2
    while True:
        n = n ** 2
        m = n + 1
        a, b, c = get_triplets(m, n)
        print(f"{b}, {a}, {c}")
        time.sleep(0.001)

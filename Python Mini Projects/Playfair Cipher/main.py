# list1 = [
#     [a, b, c, d, e],
#     [f, g, h, i, j],
#     [k, l, m, n, o],
#     [p, r, s, t, u],
#     [v, w, x, y, z],
# ]

# USE A 2D ARRAY!!!

# take in input
#   - input().lower
# remove all repeating characters
#   - convert to set
#   - convert back to string
# add each character to a list
#   - loop
#   - append
# work out remaining alphabet
#   - loop
#   - (list of alphabet).remove(i)
# then add remaining alphabet
#   - loop
#   - append

def build_alphabet() -> list:
    alphabet = []
    for i in range(65, 91):
        alphabet.append(chr(i))
    alphabet.remove("Q")
    return alphabet


def build_grid_one() -> list:
    grid_one = []
    alphabet = build_alphabet()
    seen = ""
    word = input("Input First Word: ").upper()
    for char in word:
        if char not in seen:
            seen += char
    for char in seen:
        if char in alphabet:
            alphabet.remove(char)
    for y in range(5):
        z = []
        for x in range(5):
            if seen != "":
                z.append(seen[0])
                seen = seen[1::]
            else:
                z.append(alphabet[0])
                alphabet = alphabet[1::]
        grid_one.append(z)

    print("╒═══╕╒═══╕╒═══╕╒═══╕╒═══╕")
    for y in range(5):
        for x in range(5):
            print(f"| {grid_one[y][x]} |", end="")
        print()
    print("╘═══╛╘═══╛╘═══╛╘═══╛╘═══╛")


def build_grid_two():
    grid_two = []
    alphabet = build_alphabet()
    seen = ""
    word = input("Input Second Word: ").upper()
    for char in word:
        if char not in seen:
            seen += char
    for char in seen:
        if char in alphabet:
            alphabet.remove(char)

    for y in range(5):
        z = []
        for x in range(5):
            if seen != "":
                z.append(seen[0])
                seen = seen[1::]
            else:
                z.append(alphabet[0])
                alphabet = alphabet[1::]
        z.reverse()
        grid_two.append(z)
    grid_two.reverse()

    print("╒═══╕╒═══╕╒═══╕╒═══╕╒═══╕")
    for y in range(5):
        for x in range(5):
            print(f"| {grid_two[y][x]} |", end="")
        print()
    print("╘═══╛╘═══╛╘═══╛╘═══╛╘═══╛")


build_grid_one()
build_grid_two()

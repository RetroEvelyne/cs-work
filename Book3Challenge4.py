numplate = []
for i in range(2):
    numplate.append(choice(string.ascii_uppercase))
for i in range(5):
    numplate.append(randint(0, 9))
numplate.insert(4, " ")

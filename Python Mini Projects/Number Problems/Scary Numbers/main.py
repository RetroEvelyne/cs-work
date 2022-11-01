def IsScary(num: int) -> bool:
    num = str(num)
    for i in range(len(num)):
        try:
            if num[i] == "1" and num[i+1] == "3":
                print("Scary")
                return True
        except IndexError:
            print("norm")
            return False
    print("Normal")
    return False


if __name__ == "__main__":
    IsScary(41417418781212122113637894678239)

def change(paid, cost):
    change_list = []
    coins = {"two_pound": 200, "one_pound": 100, "fifty_pence": 50, "twenty_pence": 20,
             "ten_pence": 10, "five_pence": 5, "two_pence": 2, "one_pence": 1}
    change_amount = paid - cost
    while change_amount >= coins["two_pound"]:
        change_amount -= coins["two_pound"]
        change_list.append("two_pound")
    while change_amount >= coins["one_pound"]:
        change_amount -= coins["one_pound"]
        change_list.append("one_pound")
    while change_amount >= coins["fifty_pence"]:
        change_amount -= coins["fifty_pence"]
        change_list.append("fifty_pence")
    while change_amount >= coins["twenty_pence"]:
        change_amount -= coins["twenty_pence"]
        change_list.append("twenty_pence")
    while change_amount >= coins["ten_pence"]:
        change_amount -= coins["ten_pence"]
        change_list.append("ten_pence")
    while change_amount >= coins["five_pence"]:
        change_amount -= coins["five_pence"]
        change_list.append("five_pence")
    while change_amount >= coins["two_pence"]:
        change_amount -= coins["two_pence"]
        change_list.append("two_pence")
    while change_amount >= coins["one_pence"]:
        change_amount -= coins["one_pence"]
        change_list.append("one_pence")
    if change_amount == 0:
        return (paid - cost), change_list


def main(tries=0):
    if tries >= 3:
        print("Too many tries, exiting...")
        return
    prices = {"egg_salad": 463, "ham_salad": 425, "cheese": 450, "ham": 375, "egg": 475, "humous_and_salad": 405,
              "falafel": 399, "chicken_kebab": 415, "cheese_baguette": 250, "samosa": 100}
    choice = input("What would you like to order?\n > ").lower()\
        .replace(" ", "_").replace("sandwich", "").replace("pitta", "").replace("bread", "")
    if choice not in prices:
        print("Sorry, we don't have that option.")
        main(tries + 1)
    paid = int(input("How much money have you paid?\n > "))
    if paid < prices[choice]:
        print("You haven't paid enough.")
        main(tries + 1)
    change_amount, coins = change(paid, prices[choice])
    print(f"Your change is {change_amount}p, and you will get "
          f"{str(coins).replace('[','').replace(']','').replace('_',' ')} back.")


if __name__ == "__main__":
    main()
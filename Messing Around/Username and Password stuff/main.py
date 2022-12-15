import getpass
import hashlib
import jsonUtils as jsu
from time import sleep


# Prints out text one character at a time with a short delay
# This creates a typing effect
def type_print(text: str, speed: float = 0.1):
    for char in text:
        print(char, end="", flush=True)
        sleep(speed)


# Adds a new user to the users.json file using JsonUtils
def create_user(user_data: dict):
    data: dict = jsu.openfile("users.json")
    data["users"].append(user_data)
    jsu.writetofile("users.json", data)


def login_to_user(tries: int = 0):
    if tries >= 3:
        type_print("You have reached the maximum amount of tries. \n")
        sleep(0.5)
        type_print("Exiting")
        type_print(". . .", 0.5)
        exit()
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    hashed_password: str = hashlib.sha256(password.encode()).hexdigest()
    del password
    user_data = {
        "username": username,
        "password": hashed_password
    }
    json_data: dict = jsu.openfile("users.json")
    if user_data not in json_data["users"]:
        type_print("User not found...\n")
        sleep(1)
        type_print("Do you want to create a new user? (y/n) \n ")
        choice = input(" > ")
        if choice.lower() in ["yes", "y"]:
            create_user(user_data)
            return
        else:
            login_to_user(tries + 1)
    else:
        type_print(f"Welcome back, {username}!")


if __name__ == "__main__":
    login_to_user()

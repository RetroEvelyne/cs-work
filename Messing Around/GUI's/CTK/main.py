import customtkinter as ctk
import jsonutils as jsu

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()

root.geometry("400x240")


def login_function(username: str, password: str) -> bool:
    data: dict = jsu.open_file("userdata.json")
    if username in data:
        if data[username]["Password"] == password:
            return True
        else:
            return False


username_input = ctk.CTkEntry(root, placeholder_text="Username")
username_input.pack()
password_input = ctk.CTkEntry(root, placeholder_text="Password", show="*")
password_input.pack()


login_button = ctk.CTkButton(root, text="Login", command=lambda: login_function(
    username_input.get(), password_input.get()))
login_button.pack()


root.mainloop()

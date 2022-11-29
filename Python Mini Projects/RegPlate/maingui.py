from tkinter import PhotoImage, messagebox
import customtkinter as ctk
import jsonutils as jsu
import regvalidator as rv
import findreg as fr
import sys


class Theme:
    def __init__(self, master):
        self.master = master
        self.theme_switch_image = PhotoImage(file=r"./images/theme2.png")
        self.theme_switch = ctk.CTkLabel(self.master, text="Dark")
        self.theme_button = ctk.CTkButton(self.master, image=self.theme_switch_image, text="", corner_radius=80,
                                          width=40, height=40, command=self.change_theme)
        self.theme_button.pack(side="bottom", anchor="se")

    def change_theme(self):
        if self.theme_switch.text == "Dark":
            ctk.set_default_color_theme("blue")
            ctk.set_appearance_mode("light")
            self.theme_switch.configure(text="Light")
        else:
            ctk.set_default_color_theme("dark-blue")
            ctk.set_appearance_mode("dark")
            self.theme_switch.configure(text="Dark")


class Registration:
    def __init__(self, parent):
        self.window = ctk.CTkToplevel()
        self.window.geometry("400x240")
        # self.window.title("Registration")
        # self.window.resizable(False, False)
        # self.window.iconbitmap(r"./images/icon.ico")

        self.name = ctk.CTkEntry(self.window, placeholder_text="Name")
        self.name.pack(padx=5, pady=5)
        self.phone = ctk.CTkEntry(self.window, placeholder_text="Phone Number")
        self.phone.pack(padx=5, pady=5)
        self.reg = ctk.CTkEntry(self.window, placeholder_text="Registration Number")
        self.reg.pack(padx=5, pady=5)
        self.year = ctk.CTkEntry(self.window, placeholder_text="Year")
        self.year.pack(padx=5, pady=5)
        self.submit = ctk.CTkButton(self.window, text="Submit", command=self.get_details).pack(padx=5, pady=5)

        self.details = {}

    def get_details(self) -> dict:
        self.details = {
            "name": self.name.get(),
            "phone": self.phone.get(),
            "reg": self.reg.get(),
            "year": self.year.get()
        }
        self.validate_details()

    def validate_details(self):
        if self.details["name"].isalpha() and self.details["phone"].isdigit() and self.details["year"].isdigit():
            if rv.validate_reg(self.details["reg"]):
                self.save_details()
            else:
                messagebox.showerror("Invalid Registration", "The registration number you entered is invalid")
        else:
            messagebox.showerror("Invalid Details", "You must enter a valid name, phone number and year")

    def save_details(self):
        ...


class Menu:
    def __init__(self):
        menu = ctk.CTk()
        menu.title("Registration Plate Menu")
        menu.iconbitmap("./images/icon.ico")
        menu.geometry("800x480")

        self.master = menu
        self.menu_label = ctk.CTkLabel(menu, text="Menu", text_font=("", 20))
        self.menu_label.pack()
        self.registration_button = ctk.CTkButton(menu, text="Registration", width=20, height=2, corner_radius=10,
                                                 command=self.registration)
        self.registration_button.pack(padx=10, pady=10)
        self.find_registration_button = ctk.CTkButton(menu, text="Find Registration", width=20, height=2,
                                                      corner_radius=10, command=self.find_reg)
        self.find_registration_button.pack(padx=10, pady=10)

        Theme(self.master)

    def registration(self):
        Registration(self.master)

    def find_reg(self):
        self.menu_label.configure(text="Find Registration")


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    menu_window = Menu()

    menu_window.master.mainloop()

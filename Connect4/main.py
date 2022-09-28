from tkinter import *


def wincheck(menuscreen, row, column):
    inarow = 0
    startbutt = (menuscreen.grid_slaves(row=row, column=column)[0]).cget("image")
    try:
        # Checking the one above it
        if (menuscreen.grid_slaves(row=(row-1), column=column)[0]).cget("image") == startbutt:
            inarow += 1
            newrow = row - 1
            print("hallo")
            while (menuscreen.grid_slaves(row=newrow, column=column)[0]).cget("image") == startbutt:
                inarow += 1
                newrow -= 1
            while inarow < 4:
                try:
                    if (menuscreen.grid_slaves(row=(row+1), column=column)[0]).cget("image") == startbutt:
                        inarow += 1
                except TclError:
                    pass


        if (menuscreen.grid_slaves(row=(row+1))) +
    except TclError:
        pass


def fill(row, column, menuscreen, empty, yellowfill, redfill, turn):
    value = menuscreen.grid_slaves(row=row, column=column)[0]
    if value.cget("image") != "pyimage1":
        return
    while row != 5:
        if (menuscreen.grid_slaves(row=(row + 1), column=column)[0]).cget("image") == "pyimage1":
            value = menuscreen.grid_slaves(row=(row + 1), column=column)[0]
            row += 1
        else:
            break
    if turn.cget("text") == "red":
        value.configure(image=redfill)
        turn.configure(text="yellow")
    elif turn.cget("text") == "yellow":
        value.configure(image=yellowfill)
        turn.configure(text="red")
    wincheck(menuscreen, row, column)


def creategui():
    grid = [0]
    menuscreen = Tk()
    empty = PhotoImage(file=r"H:\PogSci\emptypng.png")
    yellowfill = PhotoImage(file=r"/Connect4/yellowfill.png")
    redfill = PhotoImage(file=r"/Connect4/redfill.png")
    menuscreen.title("Connect Four!")
    menuscreen.geometry("743x638")
    turn = Label(menuscreen, text="red")
    for i in range(0, 6):
        for o in range(0, 7):
            grid.insert(o, Button(menuscreen, image=empty, command=lambda row=i, column=o: fill(row, column, menuscreen,
                                                                                                empty, yellowfill,
                                                                                                redfill, turn)))
            grid[o].grid(column=o, row=i)
    turn.grid(row=7, column=3)
    menuscreen.mainloop()


if __name__ == "__main__":
    creategui()

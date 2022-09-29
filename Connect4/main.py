from tkinter import *


def wincheck(menuscreen, row, column):
    inarow = 1
    startbutt = (menuscreen.grid_slaves(row=row, column=column)[0]).cget("image")
    forrow = row
    backrow = row
    forcol = column
    backcol = column
    # Checking the one below it
    for i in range(4):
        try:
            if (menuscreen.grid_slaves(row=(forrow + 1), column=column)[0]).cget("image") == startbutt:
                forrow += 1
                inarow += 1
            elif (menuscreen.grid_slaves(row=(backrow - 1), column=column)[0]).cget("image") == startbutt:
                backrow -= 1
                inarow += 1
        except TclError:
            pass
        except IndexError:
            pass
    if inarow >= 4:
        return "win"
    forrow = row
    backrow = row
    forcol = column
    backcol = column
    inarow = 1
    for i in range(4):
        try:
            if (menuscreen.grid_slaves(row=row, column=(forcol + 1))[0]).cget("image") == startbutt:
                forcol += 1
                inarow += 1
            if (menuscreen.grid_slaves(row=row, column=(backcol - 1))[0]).cget("image") == startbutt:
                backcol -= 1
                inarow += 1
        except TclError:
            pass
        except IndexError:
            pass
    if inarow >= 4:
        return "win"
    forrow = row
    backrow = row
    forcol = column
    backcol = column
    inarow = 1
    for i in range(4):
        try:
            if (menuscreen.grid_slaves(row=(forrow + 1), column=(forcol + 1))[0]).cget("image") == startbutt:
                forcol += 1
                forrow += 1
                inarow += 1
            if (menuscreen.grid_slaves(row=(backrow - 1), column=(backcol - 1))[0]).cget("image") == startbutt:
                backcol -= 1
                backrow -= 1
                inarow += 1
        except TclError:
            pass
        except IndexError:
            pass
    if inarow >= 4:
        return "win"
    forrow = row
    backrow = row
    forcol = column
    backcol = column
    inarow = 1
    for i in range(4):
        try:
            if (menuscreen.grid_slaves(row=(forrow + 1), column=(forcol - 1))[0]).cget("image") == startbutt:
                forcol -= 1
                forrow += 1
                inarow += 1
            if (menuscreen.grid_slaves(row=(backrow - 1), column=(backcol + 1))[0]).cget("image") == startbutt:
                backcol += 1
                backrow -= 1
                inarow += 1
        except TclError:
            pass
        except IndexError:
            pass
    if inarow >= 4:
        return "win"


def update(menuscreen, ind, framecnt, frms, win):
    frame = frms[ind]
    ind += 1
    if ind == framecnt:
        ind = 0
    win.configure(image=frame)
    menuscreen.after(100, update, menuscreen, ind, framecnt, frms, win)


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
    if wincheck(menuscreen, row, column) == "win":
        for i in range(0, 6):
            for o in range(0, 7):
                (menuscreen.grid_slaves(row=i, column=o)[0]).destroy()
        (menuscreen.grid_slaves(row=7, column=3)[0]).destroy()
        menuscreen.geometry("498x266")
        framecnt = 28
        frms = [PhotoImage(file=r"H:\PogSci\Connect4\wingif.gif", format="gif -index %i" % i) for i in range(framecnt)]
        win = Label(menuscreen)
        win.grid(row=0, column=0)
        ind = 0
        menuscreen.after(0, update, menuscreen, ind, framecnt, frms, win)


def creategui():
    grid = [0]
    menuscreen = Tk()
    empty = PhotoImage(file=r"H:\PogSci\Connect4\emptypng.png")
    yellowfill = PhotoImage(file=r"H:\PogSci\Connect4\yellowfill.png")
    redfill = PhotoImage(file=r"H:\PogSci\Connect4\redfill.png")
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

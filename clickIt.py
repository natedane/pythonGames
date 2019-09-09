from tkinter import *

window = Tk()
window.title("Testing window")
window.geometry("500x500")

class grid:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = [[1 for i in range(0,col)] for j in range (0,row)]
        self.sum = row*col
        self.buttons = [[Button() for i in range(0,col)] for j in range (0,row)]
        self.reset_button = Button()
        self.set_button = Button()
        self.e1 = Entry()
        self.e2 = Entry()
        self.label = Label()

    def reset(self, row=3, col=3):
        self.row = row
        self.col = col
        for r in self.buttons:
            for bs in r:
                bs.destroy()
        self.reset_button.destroy()
        self.set_button.destroy()
        self.e1.destroy()
        self.e2.destroy()
        self.label.destroy()
        self.label = Label()
        self.map = [[1 for i in range(0, self.col)] for j in range(0,self.row)]
        self.sum = self.row * self.col
        self.buttons = [[Button() for i in range(0, self.col)] for j in range(0, self.row)]

    def win(self):
        if self.sum == 0:
            return True


def clicked(r, c):
    switch(r,c)
    if(r>0):
        switch(r-1,c)
    if(c>0):
        switch(r,c-1)
    if(c+1<map.col):
        switch(r,c+1)
    if(r+1<map.row):
        switch(r+1,c)
    #print("{0},{1} col".format(map.sum, map.map))
    if map.win():
        winScreen = Tk()
        winScreen.title("Win window")
        winScreen.geometry("100x100")
        winLabel = Label(winScreen, text="You Win!!!").grid(row=0, column=0)
        winButton = Button(winScreen, text="OK", command=lambda:winScreen.destroy()).grid(row=1, column=0)
        winScreen.mainloop()
    window.update()


def switch(r, c):
    if map.map[r][c] == 1:
        map.map[r][c] = 0
        map.buttons[r][c].destroy()
        map.buttons[r][c] = Button(window, text="click", bg="blue", command=lambda x1=r, y1=c: clicked(x1, y1), height=5, width=10)
        map.buttons[r][c].grid(column=c, row=r)
        map.sum = map.sum - 1
    else:
        map.map[r][c] = 1
        map.buttons[r][c].destroy()
        map.buttons[r][c] = Button(window, text="click", bg="red", command=lambda x1=r, y1=c: clicked(x1, y1), height=5, width=10)
        map.buttons[r][c].grid(column=c, row=r)
        map.sum = map.sum + 1
    #print("{0}r,{1}c,{2}v,{3} map".format(r, c, map.map[r][c],map.map))


def setup(row=3, col=3, first=True):
    #print("{0}r,{1}c".format(row, col))

    if not first and row != '' and int(row) < 8 and int(col) < 8:
        row = int(row)
        col = int(col)
    else:
        row = 3
        col = 3

    if not first:
        map.reset(row, col)
    for r in range(0, row):
        for c in range(0, col):
            print("{0}r,{1}c, {2}map".format(r, c, map.map))
            map.buttons[r][c] = Button(window, text="click", bg="red", command=lambda x1=r, y1=c: clicked(x1,y1), height=5, width=10)
            map.buttons[r][c].grid(column=c, row=r)
    #map.reset_button = Button(window, text="reset button", bg="green",
    #                      command=lambda: setup(row=row, col=col, first=False), height=1, width=10)
    #map.reset_button.grid(column=0, row=row)

    map.e1 = Entry(window, text="row", width=10)
    map.e2 = Entry(window, text="col", width=10)
    map.e1.grid(column=0, row=row)
    map.e2.grid(column=1, row=row)

    map.set_button = Button(window, text="reset", bg="green", command=lambda: setup(row=map.e1.get(), col=map.e2.get(),
                                                                          first=False), height=1, width=10)
    map.set_button.grid(column=2, row=row)
    if not first:
        window.update()


map = grid(3, 3)
setup()
window.mainloop()





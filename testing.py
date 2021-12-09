from tkinter import *


class Window1:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master 

        self.label = Button(self.master, text="Example", command=self.load_new)
        self.label.pack()

    def load_new(self):
        self.label.destroy()

        # use `root` with another class
        self.another = Window2(self.master)


class Window2:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Example")
        self.label.pack()


root = Tk()
run = Window1(root)
root.mainloop()
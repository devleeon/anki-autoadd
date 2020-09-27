from tkinter import *


class ankigen_GUI(object):
    def __init__(self):
        self.app = Tk()
        self.app.title("ankigen_GUI")
        # self.app.geometry("300x300")

    def entrybox(self):
        self.ent = Entry(self.app)

    def textbox(self):
        self.txt = Text(self.app)

    def packer(self):
        self.ent.pack(side=LEFT)
        self.but.pack(side=RIGHT)

    def button(self):
        def get_word():
            word = self.ent.get()
            self.lab = Label(self.app, text=word)
            self.lab.pack()
        self.but = Button(self.app, text="input word", command=get_word)

    def App_Runner(self):
        self.app.mainloop()


root = ankigen_GUI()
root.entrybox()
root.button()
root.packer()
root.App_Runner()

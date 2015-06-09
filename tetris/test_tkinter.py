__author__ = 'Administrator'
from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

        self.fred = Button(self, fg = "red", bg = "blue")
        self.fred['text'] = 'Nash smile'
        self.fred['command'] = self.say_hi
        self.fred.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title('My first Py GUI Programing')
mainmenu=Menu(root)
root['menu']=mainmenu
app = Application(master=root)
app.mainloop()
root.destroy()
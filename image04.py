from tkinter import *

import webbrowser

class web_open3:
  def __init__(self):
     self.A = "http://www.google.ru"
  def open(self):
     webbrowser.open_new(self.A)

test = web_open3()
tablo = Tk()
tablo.title("Открыть страницу Google")
tablo.geometry('700x400+100+50')



b1 = Button(tablo, text="Google", command=test.open)
b1.pack()

tablo.mainloop()
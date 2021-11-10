#!/usr/bin/env python

# для запуска в терминале указывать полный путь к файлу
from tkinter import *  

def clicked():                   # Всталяет текст из поля Entry  в поле lbl3 при нажатии кнопки Next
    res = "Объект:  {}".format(txt.get())  
    lbl3.configure(text=res)  

from tkinter.ttk import Combobox 
  


tablo = Tk()  
tablo.title("Графическая часть Python")  
tablo.title("Графическая часть Python")
tablo.geometry('700x400+100+50')




Txt1="Присоединение1"
lbl1 = Label(tablo, text=Txt1, font=("Arial Narrow", 14))
lbl1.grid(column=0, row=0)  

txt = Entry(tablo,width=20)  
txt.grid(column=1, row=0) 

lbl2 = Label(tablo, text="Фаза", font=("Arial Narrow", 14))  
lbl2.grid(column=2, row=0)  


combo = Combobox(tablo)  
combo['values'] = (1, 2, 3, "Текст")  
combo.current(1)  # установите вариант по умолчанию  
combo.grid(column=3, row=0)  

btn = Button(tablo, text="Next", command=clicked, font=("Arial Narrow", 14))  
btn.grid(column=4, row=0)  


lbl3 = Label(tablo, text="Объект:", font=("Arial Narrow", 14))  
lbl3.grid(column=0, row=1)  




tablo.mainloop()

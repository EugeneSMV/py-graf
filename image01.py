from tkinter import *

def clicked():          # Всталяет текст из поля Entry  в поле lbl3 при нажатии кнопки Next
    res = "Объект:  {}".format(txt.get())  
    lbl3.configure(text=res)  

from tkinter.ttk import Combobox



tablo = Tk()
tablo.title("Графическая часть Python")
tablo.geometry('700x400+100+50')

title_bar = Frame(tablo, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)

lbl1 = Label(tablo, text="Ввести название ==>", font=("Times", 14), bg='Tan', fg='#ffffff')
lbl1.grid(column=0, row=0)

txt = Entry(tablo, width=20)
txt.grid(column=1, row=0) 

lbl2 = Label(tablo, text="Фаза", font=("Courier", 14), fg='Navy')
lbl2.grid(column=2, row=0)


combo = Combobox(tablo)  
combo['values'] = ("A", "B", "C", "Текст")
combo.current(0)                # установите вариант по умолчанию - номер по порядку
combo.grid(column=3, row=0)  

btn = Button(tablo, text="Next", command=clicked, font=("Helvetica", 14), bg='LightBlue', fg='Indigo'
             , activeforeground='LightYellow', activebackground='Plum')
btn.grid(column=4, row=0)  


lbl3 = Label(tablo, text="Объект:", font=("Helvetica", 14))
lbl3.grid(column=0, row=1)

tablo.mainloop()